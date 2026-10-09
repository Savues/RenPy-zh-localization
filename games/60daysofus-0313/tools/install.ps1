<#
.SYNOPSIS
    Install the 60 Days Of Us 3.1.3 Simplified Chinese patch.

.DESCRIPTION
    This is the one game in this repository whose patch cannot be delivered by
    copying files, and the reason is worth stating plainly.

    The download ships its own Simplified Chinese INSIDE game/archive.rpa, at
    tl/Chinese/. Ren`Py collects translations from the filesystem and from archives
    independently, so dropping our own game/tl/Chinese/*.rpy on top does not
    replace the archived copy -- it adds to it. Every
    `translate Chinese strings:` old/new pair then gets registered twice and

        TranslationStringRegistry.add()
        if old in self.translations: raise Exception("A translation for ... already exists.")

    fires at startup. The player never reaches the menu. A loose foo.rpy does
    not shadow an archived foo.rpy: both are read.

    The retail build ships no `archive` subcommand to delete entries, so this installer does the
    RPA-3 index surgery itself, through tools/rpa_drop_prefix.py: it drops the
    24 tl/Chinese/* entries from the index, appends the rebuilt index at the end
    of the file and patches the 34-byte header. Every surviving entry keeps the
    offset it already had, so none of the 2.5 GB of images and audio is moved,
    copied or re-compressed. The whole operation appends about 84 KB.

    The surgery needs zlib and Python's pickle, which PowerShell cannot round-trip safely. Rather than
    ask the player to install Python, this uses the interpreter the game already
    ships at lib/py3-windows-x86_64/python.exe -- verified present in this
    release as Python 3.12.7. If it is missing the installer stops and says so
    instead of guessing.

    A full copy of archive.rpa is kept at game/.zh_patch_backup/archive.rpa before
    anything is written. Run tools/uninstall.ps1 to put it back; that restores the
    file to its original length exactly.

    No Python of your own required.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 "D:\Games\60DaysOfUs-Build3.1.3(EarlyAccess)-pc"
#>
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$GameDir
)

$ErrorActionPreference = "Stop"

$here    = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoDir = Split-Path -Parent $here          # .../games/60daysofus-0313

# ---- locate the game -------------------------------------------------------
if (Test-Path -LiteralPath (Join-Path $GameDir "game")) {
    $game = Join-Path $GameDir "game"
} elseif ((Split-Path -Leaf $GameDir) -eq "game") {
    $game = $GameDir
} else {
    Write-Error "not a Ren`Py game directory (no game/ inside): $GameDir"
}
$game = (Resolve-Path -LiteralPath $game).Path

$archive = Join-Path $game "archive.rpa"
if (-not (Test-Path -LiteralPath $archive)) {
    Write-Error "no archive.rpa in $game -- this patch applies to the retail layout."
}

# ---- locate the interpreter the game already carries ----------------------
$py = Get-ChildItem -LiteralPath (Join-Path (Split-Path -Parent $game) "lib") -Recurse -Filter "python.exe" -File -ErrorAction SilentlyContinue |
      Where-Object { $_.FullName -like "*py3-windows*" } | Select-Object -First 1
if (-not $py) {
    $py = Get-ChildItem -LiteralPath (Split-Path -Parent $game) -Recurse -Filter "python.exe" -File -ErrorAction SilentlyContinue | Select-Object -First 1
}
if (-not $py) {
    Write-Error "could not find the Python that ships with this game (lib/py3-windows-x86_64/python.exe). The archive surgery needs it; refusing to install a patch that would crash at startup."
}
$surgery = Join-Path $here "rpa_drop_prefix.py"
if (-not (Test-Path -LiteralPath $surgery)) {
    Write-Error "missing $surgery"
}

# ---- manifest --------------------------------------------------------------
$manifest_ = Get-Content -LiteralPath (Join-Path $repoDir "game.json") -Raw -Encoding UTF8 | ConvertFrom-Json
if ($manifest_.patch_layout -ne "script-override") {
    Write-Error "game.json says patch_layout=$($manifest_.patch_layout); this installer only handles script-override."
    exit 1
}
if ($manifest_.font_assets.Count -ne 0) {
    Write-Error "game.json lists $($manifest_.font_assets.Count) shipped font(s); this game ships its own Source Han Serif and this patch must ship none."
    exit 1
}
$prefix = $manifest_.archive_prefix_removed

$backup    = Join-Path $game ".zh_patch_backup"
$patchGame = Join-Path $repoDir "patch\game"
$shimSrc   = Join-Path $repoDir ("patch\" + $manifest_.shim)
$touched    = New-Object System.Collections.Generic.List[string]
$introduced = New-Object System.Collections.Generic.List[string]
$compiled   = New-Object System.Collections.Generic.List[string]

function Backup-Once([string]$rel) {
    $src = Join-Path $game $rel
    $dst = Join-Path $backup $rel
    if (Test-Path -LiteralPath $dst) { return $false }
    if (-not (Test-Path -LiteralPath $src)) { return $false }
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
    Copy-Item -LiteralPath $src -Destination $dst -Force
    return $true
}

function Place([string]$rel, [string]$srcFile) {
    $existed = Test-Path -LiteralPath (Join-Path $game $rel)
    if (-not (Backup-Once $rel) -and -not $existed) { $introduced.Add($rel) }
    $dst = Join-Path $game $rel
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
    Copy-Item -LiteralPath $srcFile -Destination $dst -Force
    $touched.Add($rel)
}

Write-Host "60 Days Of Us 3.1.3 [Chinese] -> $game"
Write-Host "python: $($py.FullName)"
Write-Host ""

# ---- 1) dry run first ------------------------------------------------------
# The dry run is the default of rpa_drop_prefix.py and writes nothing. It is
# run before the backup exists so a player who cancels has lost nothing at all.
Write-Host "1/4  archive dry run"
Write-Host "--------------------"
& $py.FullName $surgery $archive --drop $prefix
if ($LASTEXITCODE -ne 0) { Write-Error "the archive dry run failed; nothing was written."; exit 1 }

# ---- 2) back the whole archive up -----------------------------------------
# 2.5 GB. It is a real cost and it is the only way this is reversible, so it is
# taken before the first byte of the archive is touched, not after.
Write-Host "2/4  archive backup"
Write-Host "---------------------"
if (Backup-Once "archive.rpa") {
    Write-Host ("  game/.zh_patch_backup/archive.rpa   {0:N0} bytes" -f (Get-Item -LiteralPath (Join-Path $backup "archive.rpa")).Length)
} else {
    Write-Host "  already backed up from an earlier run, keeping that copy"
}

# ---- 3) do the surgery -----------------------------------------------------
Write-Host "3/4  archive surgery"
Write-Host "---------------------"
& $py.FullName $surgery $archive --drop $prefix --apply --no-backup --verify 12
if ($LASTEXITCODE -ne 0) {
    Write-Error "the archive surgery failed. Restore with:"
    Write-Error ("  copy ""{0}"" over ""{1}""" -f (Join-Path $backup "archive.rpa"), $archive)
    exit 1
}

# ---- 4) the translation, then the shim -------------------------------------
Write-Host "4/4  translation"
Write-Host "-------------------"
$n = 0
Get-ChildItem -LiteralPath $patchGame -Recurse -File -Filter *.rpy | ForEach-Object {
    $rel = $_.FullName.Substring($patchGame.Length + 1)
    Place $rel $_.FullName
    $n++
}
Write-Host ("  scripts             {0,2} files" -f $n)

# Ren`Py prefers .rpyc to .rpy. Left in place, the Chinese source below is
# never read and the game keeps running the archived translation with no error
# anywhere. Backed up rather than deleted, so uninstall hands back the
# download's own set.
$c = 0
foreach ($rel in @($touched)) {
    if ($rel -notmatch '\.rpy$') { continue }
    $cpath = $rel -replace '\.rpy$', '.rpyc'
    $full  = Join-Path $game $cpath
    if (Test-Path -LiteralPath $full) {
        if (Backup-Once $cpath) { $compiled.Add($cpath) }
        Remove-Item -LiteralPath $full -Force
        $c++
    }
}
Write-Host ("  stale .rpyc moved   {0,2}" -f $c)

Place $manifest_.shim $shimSrc
Write-Host ("  shim                {0}" -f $manifest_.shim)

$k = 0
foreach ($pattern in @("bytecode-*.rpyb", "screens.rpyb")) {
    Get-ChildItem -LiteralPath (Join-Path $game "cache") -File -Filter $pattern -ErrorAction SilentlyContinue |
        ForEach-Object { Remove-Item -LiteralPath $_.FullName -Force; $k++ }
}
Write-Host ("  caches dropped      {0,2}" -f $k)

@{
    version    = 2
    game       = "60daysofus-0313"
    lang       = $manifest_.language
    archive    = "archive.rpa"
    prefix     = $prefix
    scripts    = $n
    shim       = $manifest_.shim
    compiled   = @($compiled | Sort-Object)
    introduced = @($introduced | Sort-Object)
    files      = @($touched | Sort-Object)
} | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $backup "manifest.json") -Encoding UTF8

$un = Join-Path $here "uninstall.ps1"
Write-Host ""
Write-Host "done. launch the game -- the Chinese sources are compiled on first start,"
Write-Host "which takes a while and says nothing while it does."
Write-Host ""
Write-Host "note: the archive grew by the size of its rebuilt index (about 84 KB)."
Write-Host "Nothing else in it moved, and uninstall.ps1 restores the original file."
Write-Host ""
Write-Host ('to undo:  powershell -NoProfile -ExecutionPolicy Bypass -File "{0}" "{1}"' -f $un, $GameDir)

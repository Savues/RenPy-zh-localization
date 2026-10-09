<#
.SYNOPSIS
    Install the City Devil: Restart 0.4.0 Simplified Chinese patch.

.DESCRIPTION
    City Devil: Restart ships every one of its scripts inside game/archive.rpa,
    as BOTH foo.rpy and foo.rpyc, and nothing loose in game/.  The Chinese
    translation is therefore the game's own scripts, translated: this patch
    drops eight Chinese .rpy files into game/ and a font shim alongside them.

    The part that is easy to get wrong is the .rpyc shadow.  Ren'Py builds its
    list of script files by stripping the extension, so an archived cdr_1.rpyc
    and a loose cdr_1.rpy become two entries -- ("cdr_1", None) and
    ("cdr_1", "game") -- and both are loaded, defining everything twice.  The
    loader's own de-duplication is on the full filename, and game/ is scanned
    before the archive, so a loose foo.rpy does NOT shadow an archived
    foo.rpyc.  Writing an empty foo.rpyc next to it does: the name now
    resolves to the game directory, and Ren'Py then finds no digest in the
    empty file, sees it does not match the .rpy, and recompiles from the
    Chinese source on first launch.

    That is why game.json carries an archive_shadowed list, and why the
    installer refuses to run if patch/game/ and that list disagree.

    Anything it overwrites is copied to game/.zh_patch_backup/ the first time it
    is touched.  Run tools/uninstall.ps1 to put the game back exactly as it was.

    No Python required.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 "D:\Games\CityDevilRestart-0.4.0-pc"
#>
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$GameDir
)

$ErrorActionPreference = "Stop"

$here    = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoDir = Split-Path -Parent $here          # .../games/citydevilrestart-040

# ---- locate the game -------------------------------------------------------
if (Test-Path -LiteralPath (Join-Path $GameDir "game")) {
    $game = Join-Path $GameDir "game"
} elseif ((Split-Path -Leaf $GameDir) -eq "game") {
    $game = $GameDir
} else {
    Write-Error "not a Ren'Py game directory (no game/ inside): $GameDir"
}
$game = (Resolve-Path -LiteralPath $game).Path

if (-not (Test-Path -LiteralPath (Join-Path $game "archive.rpa"))) {
    Write-Error "no archive.rpa in $game -- this patch only applies to the retail layout, where every script lives inside the archive. A game directory that already has loose .rpy files is either already patched, or not this release."
}
if (-not (Test-Path -LiteralPath (Join-Path $game "cache"))) {
    Write-Error "no cache/ in $game -- is this really the game directory?"
}

# ---- manifest --------------------------------------------------------------
$manifest_ = Get-Content -LiteralPath (Join-Path $repoDir "game.json") -Raw -Encoding UTF8 | ConvertFrom-Json
if ($manifest_.patch_layout -ne "script-override") {
    Write-Error "game.json says patch_layout=$($manifest_.patch_layout); this installer only handles script-override."
    exit 1
}
if ($manifest_.font_assets.Count -ne 0) {
    Write-Error "game.json lists $($manifest_.font_assets.Count) shipped font(s); this game resolves both faces out of archive.rpa and must ship none."
    exit 1
}

$backup    = Join-Path $game ".zh_patch_backup"
$patchGame = Join-Path $repoDir "patch\game"
$shimSrc   = Join-Path $repoDir ("patch\" + $manifest_.shim)
$touched    = New-Object System.Collections.Generic.List[string]
$introduced = New-Object System.Collections.Generic.List[string]

function Backup-Once([string]$rel) {
    $src = Join-Path $game $rel
    $dst = Join-Path $backup $rel
    if (Test-Path -LiteralPath $dst) { return $false }
    # No placeholder when the file did not exist: uninstall reads the absence
    # of a backup entry as "the patch introduced this, delete it again".
    if (-not (Test-Path -LiteralPath $src)) { return $false }
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
    Copy-Item -LiteralPath $src -Destination $dst -Force
    return $true
}

function Place([string]$rel, [string]$srcFile) {
    if (-not (Backup-Once $rel)) {
        if (-not (Test-Path -LiteralPath (Join-Path $game $rel))) {
            $introduced.Add($rel)
        }
    }
    $dst = Join-Path $game $rel
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
    Copy-Item -LiteralPath $srcFile -Destination $dst -Force
    $touched.Add($rel)
}

Write-Host "City Devil: Restart 0.4.0 [schinese] -> $game"
Write-Host ""

# ---- 1) the faces the shim points at ---------------------------------------
# Both live in archive.rpa under tl/schinese/, so there is nothing to copy and
# nothing to redistribute -- the patch points at the game's own copy.
foreach ($face in $manifest_.archive_fonts) {
    Write-Host ("  font (archive.rpa)  {0}" -f $face)
}

# ---- 2) translated scripts -------------------------------------------------
$n = 0
Get-ChildItem -LiteralPath $patchGame -Recurse -File -Filter *.rpy | ForEach-Object {
    $rel = $_.FullName.Substring($patchGame.Length + 1)
    Place $rel $_.FullName
    $n++
}
Write-Host ("  scripts             {0,2} files" -f $n)

# ---- 3) font shim ----------------------------------------------------------
Place $manifest_.shim $shimSrc
Write-Host ("  shim                {0}" -f $manifest_.shim)

# ---- 4) .rpyc shadows ------------------------------------------------------
# See the .DESCRIPTION above.  An empty file is deliberate: Ren'Py reads the
# md5 out of the last 16 bytes, finds none, and recompiles the Chinese source
# over it on the next start.
$shadowed = 0
foreach ($rel in $manifest_.archive_shadowed) {
    if (-not (Test-Path -LiteralPath (Join-Path $patchGame $rel))) {
        Write-Error "game.json lists $rel as archive-shadowed but patch/game/$rel does not exist."
        exit 1
    }
    $base = $rel -replace '\.rpy$', ''
    $c = Join-Path $game ($base + '.rpyc')
    if (Test-Path -LiteralPath $c) {
        # Already there.  On the retail layout nothing is loose at all and this
        # branch never runs; it exists for a game directory that already had
        # bytecode on disk.  Keep the file -- Ren'Py recompiles it on the next
        # start because its digest no longer matches -- but put a copy aside,
        # because running the game overwrites it and uninstall has to hand the
        # original back rather than leave stale bytecode behind.
        if ((Get-Item -LiteralPath $c).Length -gt 0) {
            if (Backup-Once ($base + '.rpyc')) { $touched.Add($base + '.rpyc') }
            Write-Host ("  ~ {0,-14} existing .rpyc kept and backed up; its digest no longer matches" -f ($base + '.rpyc'))
        }
    } else {
        New-Item -ItemType File -Path $c | Out-Null
        $introduced.Add($base + '.rpyc')
        Write-Host ("  + {0,-14} empty shadow, so the archived .rpyc is skipped" -f ($base + '.rpyc'))
    }
    $shadowed++
}
Write-Host ("  .rpyc shadows       {0,2} files" -f $shadowed)

# ---- 5) drop the derived caches -------------------------------------------
# bytecode-*.rpyb caches compiled python keyed by script version; screens.rpyb
# caches the parsed screen language.  Both are rebuilt on the first start, and
# a stale one keyed to the English scripts is not worth debugging.
$k = 0
foreach ($pattern in @("bytecode-*.rpyb", "screens.rpyb")) {
    Get-ChildItem -LiteralPath (Join-Path $game "cache") -File -Filter $pattern -ErrorAction SilentlyContinue |
        ForEach-Object {
            Remove-Item -LiteralPath $_.FullName -Force
            Write-Host ("  - cache/{0}" -f $_.Name)
            $k++
        }
}
Write-Host ("  caches dropped      {0,2}" -f $k)

# ---- 6) record what we did -------------------------------------------------
# "files" is the list uninstall reads, so either installer can be undone by
# either uninstaller.
@{
    version    = 2
    game       = "citydevilrestart-040"
    lang       = $manifest_.language
    scripts    = $n
    shim       = $manifest_.shim
    shadowed   = $shadowed
    introduced = @($introduced | Sort-Object)
    files      = @($touched | Sort-Object)
} | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $backup "manifest.json") -Encoding UTF8

$un = Join-Path $here "uninstall.ps1"
Write-Host ""
Write-Host "done. launch the game -- the Chinese scripts are compiled on first start,"
Write-Host "which takes a while and says nothing while it does."
Write-Host ""
Write-Host ('to undo:  powershell -NoProfile -ExecutionPolicy Bypass -File "{0}" "{1}"' -f $un, $gameDir)

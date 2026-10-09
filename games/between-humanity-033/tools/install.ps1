<#
.SYNOPSIS
    Install the Between Humanity 0.3.3 Simplified Chinese patch.

.DESCRIPTION
    The download already ships a Simplified Chinese translation at
    game/tl/chinese/, and the game names that language "chinese" -- so this
    patch does not add a language.  It revises the text already in that tree
    and copies it back over itself, then sets config.language so the player
    does not have to go through the language picker first.

    The part that is easy to get wrong is the .rpyc.  The download carries a
    compiled .rpyc beside every .rpy in game/tl/chinese/, and Ren'Py loads
    bytecode in preference to source.  Copy the Chinese .rpy over the top and
    leave the old .rpyc in place and the game keeps running the publisher's
    text with no error anywhere -- so every .rpyc that sits next to a file this
    patch writes is moved aside before the .rpy goes down.

    Anything overwritten is copied to game/.zh_patch_backup/ the first time it
    is touched, the compiled files included, so uninstall hands back the exact
    layout the download shipped.  Run tools/uninstall.ps1 to undo.

    No Python required.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 "D:\Games\Between-Humanity-0.3.3-pc"
#>
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$GameDir
)

$ErrorActionPreference = "Stop"

$here    = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoDir = Split-Path -Parent $here          # .../games/between-humanity-033

# ---- locate the game -------------------------------------------------------
if (Test-Path -LiteralPath (Join-Path $GameDir "game")) {
    $game = Join-Path $GameDir "game"
} elseif ((Split-Path -Leaf $GameDir) -eq "game") {
    $game = $GameDir
} else {
    Write-Error "not a Ren'Py game directory (no game/ inside): $GameDir"
}
$game = (Resolve-Path -LiteralPath $game).Path

if (-not (Test-Path -LiteralPath (Join-Path $game "scripts.rpa"))) {
    Write-Error "no scripts.rpa in $game -- this patch applies to the retail layout, where the English scripts live in scripts.rpa and the translation sits loose at game/tl/chinese/."
}
$tlDir = Join-Path $game "tl\chinese"
if (-not (Test-Path -LiteralPath $tlDir)) {
    Write-Error "no game/tl/chinese/ in $game -- the download ships a Simplified Chinese tree and this patch revises it in place. A directory without one is not this release."
}

# ---- manifest --------------------------------------------------------------
$manifest_ = Get-Content -LiteralPath (Join-Path $repoDir "game.json") -Raw -Encoding UTF8 | ConvertFrom-Json
if ($manifest_.patch_layout -ne "script-override") {
    Write-Error "game.json says patch_layout=$($manifest_.patch_layout); this installer only handles script-override."
    exit 1
}
if ($manifest_.language -ne "chinese") {
    Write-Error "game.json says language=$($manifest_.language). This patch writes game/tl/$($manifest_.language)/, which would be a second language rather than a revision of the one the game already has."
    exit 1
}
if ($manifest_.font_assets.Count -ne 0) {
    Write-Error "game.json lists $($manifest_.font_assets.Count) shipped font(s); the game's own CJK faces already work and this patch ships none."
    exit 1
}

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
    # No placeholder when the file did not exist: uninstall reads the absence
    # of a backup entry as "the patch introduced this, delete it again".
    if (-not (Test-Path -LiteralPath $src)) { return $false }
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
    Copy-Item -LiteralPath $src -Destination $dst -Force
    return $true
}

function Place([string]$rel, [string]$srcFile) {
    $existed = Test-Path -LiteralPath (Join-Path $game $rel)
    if (-not (Backup-Once $rel) -and -not $existed) {
        $introduced.Add($rel)
    }
    $dst = Join-Path $game $rel
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
    Copy-Item -LiteralPath $srcFile -Destination $dst -Force
    $touched.Add($rel)
}

Write-Host "Between Humanity 0.3.3 [$($manifest_.language)] -> $game"
Write-Host ""

# ---- 1) the revised tree, file by file ------------------------------------
# Copied one at a time rather than as a tree replacement: the game ships 134
# files and this patch carries all 134, but a wholesale delete would throw away
# the .rpyc set that step 2 depends on and any file the player added.
$n = 0
Get-ChildItem -LiteralPath $patchGame -Recurse -File -Filter *.rpy | ForEach-Object {
    $rel = $_.FullName.Substring($patchGame.Length + 1)
    Place $rel $_.FullName
    $n++
}
Write-Host ("  scripts             {0,2} files" -f $n)

# ---- 2) move the stale bytecode aside -------------------------------------
# Ren'Py prefers .rpyc to .rpy.  Left in place, the Chinese source below is
# never read.  These are backed up rather than deleted: the game regenerates
# them on the next start, and uninstall has to put the download's own back.
$c = 0
foreach ($rel in @($touched)) {
    if ($rel -notmatch '\.rpy$') { continue }
    $cpath = $rel -replace '\.rpy$', '.rpyc'
    $full  = Join-Path $game $cpath
    if (Test-Path -LiteralPath $full) {
        if (Backup-Once $cpath) { $compiled.Add($cpath) }
        Remove-Item -LiteralPath $full -Force
        $c++
    } elseif (Backup-Once $cpath) {
        # Nothing to remove, but the player had one at some point.
        $compiled.Add($cpath)
    }
}
Write-Host ("  stale .rpyc moved   {0,2}" -f $c)

# ---- 3) force the language -------------------------------------------------
Place $manifest_.shim $shimSrc
Write-Host ("  shim                {0}" -f $manifest_.shim)

# ---- 4) drop the derived caches -------------------------------------------
# bytecode-*.rpyb caches compiled python keyed by script version; screens.rpyb
# caches the parsed screen language.  Both are rebuilt on the first start, and
# one keyed to the publisher's scripts is not worth debugging.
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

# ---- 5) record what we did -------------------------------------------------
@{
    version    = 2
    game       = "between-humanity-033"
    lang       = $manifest_.language
    scripts    = $n
    shim       = $manifest_.shim
    compiled   = @($compiled | Sort-Object)
    introduced = @($introduced | Sort-Object)
    files      = @($touched | Sort-Object)
} | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $backup "manifest.json") -Encoding UTF8

$un = Join-Path $here "uninstall.ps1"
Write-Host ""
Write-Host "done. launch the game; the Chinese sources are compiled on first start,"
Write-Host "which takes a while and says nothing while it does."
Write-Host ""
Write-Host "note: the game itself says some languages are partly or wholly"
Write-Host "AI-translated, and credits its translators in the About screen. That is"
Write-Host "still true of the base text this patch revises, so the notice is left alone."
Write-Host ""
Write-Host ('to undo:  powershell -NoProfile -ExecutionPolicy Bypass -File "{0}" "{1}"' -f $un, $GameDir)

<#
.SYNOPSIS
    Install the Scions of the Divine 0.1 Simplified Chinese patch.

.DESCRIPTION
    Scions of the Divine ships its scripts inside game/archive.rpa and has no
    Ren'Py translation tree -- game/tl/ holds nothing but None/common.rpym.
    This patch therefore replaces 27 of the game's own .rpy files with Chinese
    ones; there is no translate tree to drop into game/tl/.

    Ren'Py prefers a loose game/<path>.rpy over the same path inside
    archive.rpa, so copying them out is all it takes -- nothing inside the
    archive is rewritten, and the 1.1 GB file is left exactly as it shipped.

    Anything this patch overwrites is copied to game/.zh_patch_backup/ the
    first time it is touched. Run tools/uninstall.ps1 to put the game back
    exactly as it was.

    No Python required.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 "D:\Games\ScionsoftheDivine-v0.1-pc"
#>
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$GameDir
)

$ErrorActionPreference = "Stop"

$here    = Split-Path -Parent $MyInvocation.MyCommand.Path
$gameDir = $GameDir.TrimEnd('\')
$repoDir = Split-Path -Parent $here          # .../games/scionsofthedivine-01

# ---- locate the game -------------------------------------------------------
if (Test-Path -LiteralPath (Join-Path $gameDir "game")) {
    $game = Join-Path $gameDir "game"
} elseif ((Split-Path -Leaf $gameDir) -eq "game") {
    $game = $gameDir
} else {
    Write-Error "not a Ren'Py game directory (no game/ inside): $gameDir"
}
# This game keeps options.rpy at scripts/systems/, so identify it by the two
# files that are always loose at the game root instead.
foreach ($probe in @("script_version.txt", "archive.rpa")) {
    if (-not (Test-Path -LiteralPath (Join-Path $game $probe))) {
        Write-Error "no $probe in $game -- is this really Scions of the Divine 0.1?"
    }
}

$manifest_ = Get-Content -LiteralPath (Join-Path $repoDir "game.json") -Raw -Encoding UTF8 | ConvertFrom-Json
if ($manifest_.patch_layout -ne "script-override") {
    Write-Error "game.json says patch_layout=$($manifest_.patch_layout); this installer only handles script-override."
    exit 1
}

$backup = Join-Path $game ".zh_patch_backup"
$patchGame = Join-Path $repoDir "patch\game"
$shimRel   = $manifest_.shim
$shimSrc   = Join-Path $repoDir "patch\$shimRel"
$touched   = New-Object System.Collections.Generic.List[string]

function Backup-Once([string]$rel) {
    $src = Join-Path $game $rel
    $dst = Join-Path $backup $rel
    if (Test-Path -LiteralPath $dst) { return $false }   # first touch only
    # Nothing to do when the file did not exist: tools/uninstall.py reads the
    # absence of a backup entry as "the patch introduced this file, delete it
    # again on uninstall". Leaving no placeholder keeps the backup directory
    # free of empty scaffolding, same convention as install.py.
    if (-not (Test-Path -LiteralPath $src)) { return $false }
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
    Copy-Item -LiteralPath $src -Destination $dst -Force
    return $true
}

Write-Host "Scions of the Divine 0.1 [$($manifest_.language)] -> $game"

# ---- 1) translated scripts -------------------------------------------------
$n = 0
Get-ChildItem -LiteralPath $patchGame -Recurse -File -Filter *.rpy | ForEach-Object {
    $rel = $_.FullName.Substring($patchGame.Length + 1)
    Backup-Once $rel | Out-Null
    $dst = Join-Path $game $rel
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
    Copy-Item -LiteralPath $_.FullName -Destination $dst -Force
    $touched.Add(($rel -replace '\\', '/'))
    $n++
}
Write-Host ("  scripts            {0,3} files" -f $n)

# ---- 2) font shim ----------------------------------------------------------
Backup-Once $shimRel | Out-Null
Copy-Item -LiteralPath $shimSrc -Destination (Join-Path $game $shimRel) -Force
$touched.Add($shimRel)
Write-Host "  shim               $shimRel"

# ---- 3) CJK font -----------------------------------------------------------
$fonts = 0
foreach ($fa in $manifest_.font_assets) {
    $srcFace = Join-Path $repoDir ($fa.path -replace '/', '\')
    foreach ($name in $fa.names) {
        $rel = "fonts/$name"
        Backup-Once $rel | Out-Null
        New-Item -ItemType Directory -Force -Path (Join-Path $game "fonts") | Out-Null
        Copy-Item -LiteralPath $srcFace -Destination (Join-Path $game "fonts\$name") -Force
        $touched.Add($rel)
        $fonts++
    }
}
Write-Host ("  fonts              {0,2} files" -f $fonts)

# ---- 4) drop stale bytecode ------------------------------------------------
# Ren'Py prefers .rpyc; a stale one silently wins over the .rpy we just wrote.
# The game's own scripts live in archive.rpa, so the compiled bytecode of the
# English originals is in there too and cannot be reached from disk. What we
# CAN clean is the bytecode of a previous run of this patch.
$k = 0
Get-ChildItem -LiteralPath $game -Recurse -File |
    Where-Object { $_.Extension -in ".rpyc", ".rpymc" } |
    ForEach-Object {
    # .rpyc is compiled from .rpy, .rpymc from .rpym.  Truncating the
    # extension would leave "story", not "story.rpy", so rename it instead.
    $srcExt = if ($_.Extension -eq ".rpyc") { ".rpy" } else { ".rpym" }
    $base = [System.IO.Path]::ChangeExtension($_.FullName, $srcExt)
    if (Test-Path -LiteralPath $base) {
        Remove-Item -LiteralPath $_.FullName -Force
        $k++
    }
}
Write-Host ("  removed bytecode   {0,3} .rpyc/.rpymc" -f $k)

# ---- 5) record what we did -------------------------------------------------
# "files" is the same list tools/install.py v2 and tools/uninstall.py read, so
# either installer can be undone with either uninstaller.
@{
    version = 2
    game    = "scionsofthedivine-01"
    lang    = $manifest_.language
    scripts = $n
    shim    = $shimRel
    files   = @($touched | Sort-Object)
} | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $backup "manifest.json") -Encoding UTF8

Write-Host ""
Write-Host "done. launch the game -- the Chinese scripts are compiled on first start."
Write-Host ""
Write-Host "to undo:  powershell -NoProfile -ExecutionPolicy Bypass -File `"$here\uninstall.ps1`" `"$gameDir`""
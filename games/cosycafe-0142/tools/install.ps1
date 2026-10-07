<#
.SYNOPSIS
    Install the Cosy Cafe 0.14.2 Simplified Chinese patch.

.DESCRIPTION
    Cosy Cafe does not use Ren'Py translations.  This patch replaces 27 of the
    game's own .rpy files with Chinese ones, so there is no translate tree to
    drop into game/tl/ -- the scripts themselves are the patch.

    Anything it overwrites is copied to game/.zh_patch_backup/ the first time it
    is touched.  Run tools/uninstall.ps1 to put the game back exactly as it was.

    No Python required.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 "D:\Games\CosyCafe-0.14.2-pc"
#>
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$GameDir
)

$ErrorActionPreference = "Stop"

$here    = Split-Path -Parent $MyInvocation.MyCommand.Path
$gameDir = $GameDir.TrimEnd('\')
$repoDir = Split-Path -Parent $here          # .../games/cosycafe-0142

# ---- locate the game -------------------------------------------------------
if (Test-Path -LiteralPath (Join-Path $gameDir "game")) {
    $game = Join-Path $gameDir "game"
} elseif ((Split-Path -Leaf $gameDir) -eq "game") {
    $game = $gameDir
} else {
    Write-Error "not a Ren'Py game directory (no game/ inside): $gameDir"
}
if (-not (Test-Path -LiteralPath (Join-Path $game "options.rpy")) -and
    -not (Test-Path -LiteralPath (Join-Path $game "options.rpyc"))) {
    Write-Error "no options.rpy in $game -- is this really the game directory?"
}

$backup = Join-Path $game ".zh_patch_backup"
$patchGame = Join-Path $repoDir "patch\game"
$shimSrc   = Join-Path $repoDir "patch\zz_zh_locale.rpy"
$fontSrc   = Join-Path $repoDir "assets\fonts"

function Backup-Once([string]$rel) {
    $src = Join-Path $game $rel
    $dst = Join-Path $backup $rel
    if (Test-Path -LiteralPath $dst) { return $false }   # first touch only
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
    if (Test-Path -LiteralPath $src) {
        if ((Get-Item -LiteralPath $src).PSIsContainer) {
            Copy-Item -LiteralPath $src -Destination $dst -Recurse -Force
        } else {
            Copy-Item -LiteralPath $src -Destination $dst -Force
        }
    } else {
        New-Item -ItemType File -Force -Path $dst | Out-Null   # tombstone: did not exist
    }
    return $true
}

Write-Host "Cosy Cafe 0.14.2 [schinese] -> $game"

# ---- 1) translated scripts -------------------------------------------------
$n = 0
Get-ChildItem -LiteralPath $patchGame -Recurse -File -Filter *.rpy | ForEach-Object {
    $rel = $_.FullName.Substring($patchGame.Length + 1)
    Backup-Once $rel | Out-Null
    $dst = Join-Path $game $rel
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
    Copy-Item -LiteralPath $_.FullName -Destination $dst -Force
    $n++
}
Write-Host ("  scripts            {0,3} files" -f $n)

# ---- 2) font shim ----------------------------------------------------------
$shimRel = "zz_zh_locale.rpy"
Backup-Once $shimRel | Out-Null
Copy-Item -LiteralPath $shimSrc -Destination (Join-Path $game $shimRel) -Force
Write-Host "  shim               $shimRel"

# ---- 3) CJK font -----------------------------------------------------------
$fonts = 0
foreach ($f in @("MiSans-Regular.ttf", "MiSans-Bold.ttf")) {
    $rel = "fonts/$f"
    Backup-Once $rel | Out-Null
    New-Item -ItemType Directory -Force -Path (Join-Path $game "fonts") | Out-Null
    Copy-Item -LiteralPath (Join-Path $fontSrc $f) -Destination (Join-Path $game "fonts\$f") -Force
    $fonts++
}
Write-Host ("  fonts              {0,2} files" -f $fonts)

# ---- 4) drop stale bytecode ------------------------------------------------
# Ren'Py prefers .rpyc; a stale one silently wins over the .rpy we just wrote.
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
@{ version = 1; game = "cosycafe-0142"; scripts = $n; fonts = 2; shim = $shimRel } |
    ConvertTo-Json | Set-Content -LiteralPath (Join-Path $backup "manifest.json") -Encoding UTF8

Write-Host ""
Write-Host "done. launch the game -- the Chinese scripts are compiled on first start."
Write-Host ""
Write-Host "to undo:  powershell -NoProfile -ExecutionPolicy Bypass -File `"$here\uninstall.ps1`" `"$gameDir`""

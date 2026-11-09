<#
.SYNOPSIS
    Install the WildCats 0.4 Multi-Mod (Simplified Chinese) patch.

.DESCRIPTION
    Installs the BladeSSR Multi-Mod (Cheat Menu & Walkthrough hints) adapted
    for the Simplified Chinese version of WildCats 0.4.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 "D:\Games\WildCats-0.4-pc"
#>
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$GameDir
)

$ErrorActionPreference = "Stop"

$here    = Split-Path -Parent $MyInvocation.MyCommand.Path
$gameDir = $GameDir.TrimEnd('\')
$repoDir = Split-Path -Parent $here

if (Test-Path -LiteralPath (Join-Path $gameDir "game")) {
    $game = Join-Path $gameDir "game"
} elseif ((Split-Path -Leaf $gameDir) -eq "game") {
    $game = $gameDir
} else {
    Write-Error "not a Ren'Py game directory (no game/ inside): $gameDir"
}

$patchSrc = Join-Path $repoDir "patch\game\BladeSSRMod"
$patchDst = Join-Path $game "BladeSSRMod"

Write-Host "Installing BladeSSRMod to $patchDst..."
Copy-Item -LiteralPath $patchSrc -Destination $patchDst -Recurse -Force

$shimSrc = Join-Path $repoDir "patch\zz_zh_mod.rpy"
$shimDst = Join-Path $game "zz_zh_mod.rpy"
Copy-Item -LiteralPath $shimSrc -Destination $shimDst -Force

Write-Host "Installation complete! Start the game and switch language to Chinese."

<#
.SYNOPSIS
    Remove the Scions of the Divine 0.1 Simplified Chinese patch and put the game back.

.DESCRIPTION
    Works from the file list install.ps1 recorded in game/.zh_patch_backup/manifest.json,
    which is the same list tools/uninstall.py reads -- so either uninstaller undoes
    either installer.

    For each file the patch wrote:
      * a non-empty backup exists  -> it is copied back, byte for byte
      * no backup exists           -> the patch introduced the file, so it is deleted

    That second case is the common one here. This game keeps every script inside
    game/archive.rpa, so the 28 .rpy files the patch drops in did not exist on disk
    before; uninstalling has to take them away again or Ren'Py would keep loading
    the Chinese copies over the archive's English originals.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File uninstall.ps1 "D:\Games\ScionsoftheDivine-v0.1-pc"
#>
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$GameDir
)

$ErrorActionPreference = "Stop"

$gameDir = $GameDir.TrimEnd('\')
if (Test-Path -LiteralPath (Join-Path $gameDir "game")) {
    $game = Join-Path $gameDir "game"
} elseif ((Split-Path -Leaf $gameDir) -eq "game") {
    $game = $gameDir
} else {
    Write-Error "not a Ren'Py game directory (no game/ inside): $gameDir"
}

$backup = Join-Path $game ".zh_patch_backup"
$manifestPath = Join-Path $backup "manifest.json"
if (-not (Test-Path -LiteralPath $manifestPath)) {
    Write-Error "no $manifestPath -- install.ps1 was never run here."
}

$manifest_ = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
if (-not $manifest_.files) {
    Write-Error "manifest.json has no file list; cannot undo safely."
    exit 1
}

$restored = 0
$removed  = 0

foreach ($rel in $manifest_.files) {
    $dst = Join-Path $game ($rel -replace '/', '\')
    $src = Join-Path $backup ($rel -replace '/', '\')
    if ((Test-Path -LiteralPath $src) -and (Get-Item -LiteralPath $src).Length -gt 0) {
        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
        Copy-Item -LiteralPath $src -Destination $dst -Force
        $restored++
    } elseif (Test-Path -LiteralPath $dst) {
        Remove-Item -LiteralPath $dst -Force
        $removed++
    }
    # Recompiled bytecode now belongs to the Chinese scripts; drop it so
    # Ren'Py rebuilds from whatever is there after this.
    foreach ($ext in @(".rpyc", ".rpymc")) {
        $stale = [System.IO.Path]::ChangeExtension($dst, $ext.TrimStart('.'))
        if (Test-Path -LiteralPath $stale) { Remove-Item -LiteralPath $stale -Force }
    }
}

# Prune directories the installer created, bottom-up.
foreach ($dir in (Get-ChildItem -LiteralPath $game -Recurse -Directory | Sort-Object { $_.FullName.Length } -Descending)) {
    if ((Split-Path -Leaf $dir.FullName) -eq ".zh_patch_backup") { continue }
    if (-not (Get-ChildItem -LiteralPath $dir.FullName -Force | Select-Object -First 1)) {
        Remove-Item -LiteralPath $dir.FullName -Force
    }
}

Remove-Item -LiteralPath $backup -Recurse -Force

Write-Host "restored $restored file(s), removed $removed patch-only file(s)"
Write-Host "done -- the game is back to its original English state."
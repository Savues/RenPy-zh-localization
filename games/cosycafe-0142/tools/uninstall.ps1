<#
.SYNOPSIS
    Remove the Cosy Cafe 0.14.2 Simplified Chinese patch and put the game back.

.DESCRIPTION
    Restores every file install.ps1 overwrote from game/.zh_patch_backup/.
    Files the patch created (and therefore did not overwrite) are removed.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File uninstall.ps1 "D:\Games\CosyCafe-0.14.2-pc"
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
if (-not (Test-Path -LiteralPath $backup)) {
    Write-Error "no backup at $backup -- install.ps1 was never run here."
}

$restored = 0
$removed  = 0

Get-ChildItem -LiteralPath $backup -Recurse -File | ForEach-Object {
    if ($_.Name -eq "manifest.json") { return }
    $rel = $_.FullName.Substring($backup.Length + 1)
    $dst = Join-Path $game $rel
    if ($_.Length -eq 0) {
        # zero-length tombstone: this file did not exist before the patch
        if (Test-Path -LiteralPath $dst) {
            Remove-Item -LiteralPath $dst -Force
            $removed++
        }
    } else {
        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
        Copy-Item -LiteralPath $_.FullName -Destination $dst -Force
        $restored++
    }
}

# Recompiled bytecode now belongs to the Chinese scripts; drop it so Ren'Py
# rebuilds from the restored English sources.
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

Remove-Item -LiteralPath $backup -Recurse -Force

Write-Host "restored $restored file(s), removed $removed patch-only file(s), dropped $k stale bytecode file(s)"
Write-Host "done -- the game is back to its original English state."

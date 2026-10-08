<#
.SYNOPSIS
    Remove the Wartribe Academy 2.0.3 Simplified Chinese patch and put the game back.

.DESCRIPTION
    Restores every file install.ps1 overwrote from game/.zh_patch_backup/, and
    deletes the files the patch introduced (the shim, the three fonts and their
    directory).  The list comes from the manifest the installer wrote, so it
    survives the patch tree being edited between install and uninstall.

    Ren'Py's own tools/uninstall.py does the same job from the same manifest if
    you would rather not run PowerShell.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File uninstall.ps1 "D:\Games\WartribeAcademy-2.0.3-pc"
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

# The installer records what it wrote.  Anything with a backup entry is put
# back; anything without one did not exist before and is deleted instead.
# Reading the manifest rather than walking the backup directory is what makes
# the second case work: the shim and the three fonts leave no backup behind.
$manifestPath = Join-Path $backup "manifest.json"
$rels = @()
if (Test-Path -LiteralPath $manifestPath) {
    $m = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($m.files) { $rels = @($m.files) }
}

if ($rels.Count -eq 0) {
    # Manifest missing or empty: fall back to whatever was backed up.
    Get-ChildItem -LiteralPath $backup -Recurse -File | ForEach-Object {
        if ($_.Name -eq "manifest.json") { return }
        $rels += ($_.FullName.Substring($backup.Length + 1) -replace '\\', '/')
    }
}

foreach ($rel in ($rels | Sort-Object -Unique)) {
    $src = Join-Path $backup ($rel -replace '/', '\')
    $dst = Join-Path $game ($rel -replace '/', '\')
    if (Test-Path -LiteralPath $src) {
        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
        Copy-Item -LiteralPath $src -Destination $dst -Force
        $restored++
        Write-Host ("  restored  {0}" -f $rel)
    } elseif (Test-Path -LiteralPath $dst) {
        Remove-Item -LiteralPath $dst -Force
        $removed++
        Write-Host ("  removed   {0}" -f $rel)
    }
    # Recompiled bytecode belongs to whichever scripts are in place now.
    foreach ($ext in ".rpyc", ".rpymc") {
        $stale = [System.IO.Path]::ChangeExtension($dst, $ext)
        if (Test-Path -LiteralPath $stale) {
            Remove-Item -LiteralPath $stale -Force
        }
    }
}

# Drop bytecode that no longer has a source, e.g. from a file the patch added.
$k = 0
Get-ChildItem -LiteralPath $game -Recurse -File |
    Where-Object { $_.Extension -in ".rpyc", ".rpymc" } |
    ForEach-Object {
    $srcExt = if ($_.Extension -eq ".rpyc") { ".rpy" } else { ".rpym" }
    if (Test-Path -LiteralPath ([System.IO.Path]::ChangeExtension($_.FullName, $srcExt))) {
        Remove-Item -LiteralPath $_.FullName -Force
        $k++
    }
}

# Prune directories the installer created, bottom-up, so nothing is left empty.
foreach ($dir in (Get-ChildItem -LiteralPath $game -Recurse -Directory | Sort-Object { $_.FullName.Length } -Descending)) {
    if (-not (Get-ChildItem -LiteralPath $dir.FullName -Force)) {
        Remove-Item -LiteralPath $dir.FullName -Force
    }
}
if (Test-Path -LiteralPath (Join-Path $game "fonts")) {
    if (-not (Get-ChildItem -LiteralPath (Join-Path $game "fonts") -Force)) {
        Remove-Item -LiteralPath (Join-Path $game "fonts") -Force
    }
}

Remove-Item -LiteralPath $backup -Recurse -Force

Write-Host ""
Write-Host "restored $restored file(s), removed $removed patch-only file(s), dropped $k stale bytecode file(s)"
Write-Host "done -- the game is back to its original English state."
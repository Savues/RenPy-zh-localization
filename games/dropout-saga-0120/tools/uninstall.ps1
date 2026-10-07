<#
.SYNOPSIS
    Remove the DropOut Saga 0.12.0b Simplified Chinese patch and put the game back.

.DESCRIPTION
    Restores every file install.ps1 overwrote from game/.zh_patch_backup/.
    Files the patch created (and therefore did not overwrite) are removed.

    A mod installed with -WithMod is restored too: the English .rpyc went into
    the same backup tree, so it comes back without this script needing to know
    anything about the mod.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File uninstall.ps1 "D:\Games\DropOutSaga-0.12.0b-pc"
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

$manifestPath = Join-Path $backup "manifest.json"
if (-not (Test-Path -LiteralPath $manifestPath)) {
    Write-Error "$manifestPath is missing -- the backup is not one this script wrote."
}

# What the patch listed but did not overwrite is exactly what it created, and
# that is what has to go.  The backup tree cannot say so on its own: it only
# holds entries for files that used to exist.
$m = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
$created = @($m.files | Where-Object { -not (Test-Path -LiteralPath (Join-Path $backup $_)) })

$restored = 0
$removed  = 0

Get-ChildItem -LiteralPath $backup -Recurse -File | ForEach-Object {
    if ($_.Name -eq "manifest.json") { return }
    $rel = $_.FullName.Substring($backup.Length + 1)
    $dst = Join-Path $game $rel
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
    Copy-Item -LiteralPath $_.FullName -Destination $dst -Force
    $restored++
}

foreach ($rel in $created) {
    $dst = Join-Path $game $rel
    if (Test-Path -LiteralPath $dst) {
        Remove-Item -LiteralPath $dst -Recurse -Force
        $removed++
    }
}

# Bytecode the patch's own scripts generated belongs to the Chinese patch, so
# it goes.  Anything with a backup entry was just restored to the bytes the
# game shipped with and stays -- deleting it would lose the pristine state for
# no reason.  This is also what keeps game/mod/*.rpyc safe: it has a backup
# entry, and no .rpy sibling to key off.  The backup tree is excluded for
# the same reason install.ps1 excludes it: it holds .rpyc of its own.
$k = 0
Get-ChildItem -LiteralPath $game -Recurse -File |
    Where-Object { $_.Extension -in ".rpyc", ".rpymc" } |
    Where-Object { -not $_.FullName.StartsWith($backup + "\") } |
    ForEach-Object {
    $rel = $_.FullName.Substring($game.Length + 1)
    if (-not (Test-Path -LiteralPath (Join-Path $backup $rel))) {
        Remove-Item -LiteralPath $_.FullName -Force
        $k++
    }
}

# The patch shipped no directory the game does not have, but an interrupted
# install.ps1 run can leave the mod build directory behind.
$build = Join-Path $game ".zh_mod_build"
if (Test-Path -LiteralPath $build) {
    Remove-Item -LiteralPath $build -Recurse -Force
    Write-Host "removed leftover mod build directory"
}

Remove-Item -LiteralPath $backup -Recurse -Force

# Directories the patch brought with it (game/Fonts) are now empty.  Walk each
# removed file's parents and drop the ones that are, so a fresh uninstall does
# not leave scaffolding behind -- but never a directory the game came with.
foreach ($rel in $created) {
    $dir = Split-Path -Parent (Join-Path $game $rel)
    while ($dir -and $dir.StartsWith($game) -and $dir -ne $game) {
        if (-not (Test-Path -LiteralPath $dir)) { $dir = Split-Path -Parent $dir; continue }
        if (Get-ChildItem -LiteralPath $dir -Force) { break }   # not ours to remove
        Remove-Item -LiteralPath $dir -Force
        $dir = Split-Path -Parent $dir
    }
}

Write-Host "restored $restored file(s), removed $removed patch-only file(s), dropped $k stale bytecode file(s)"
Write-Host "done -- the game is back to its original English state."

<#
.SYNOPSIS
    Remove the City Devil: Restart 0.4.0 Simplified Chinese patch and put the game back.

.DESCRIPTION
    Puts back every file install.ps1 overwrote, and deletes every file it
    introduced -- the eight Chinese scripts, the font shim, and the empty .rpyc
    shadows that exist only to hide the archive's own .rpyc.  What to restore
    and what to delete is read from the manifest the installer wrote, so it
    survives the patch tree being edited between install and uninstall.

    On the retail layout this returns game/ to having no loose scripts at all,
    which is the state the archive expects: the English .rpy and .rpyc come
    back out of archive.rpa and Ren'Py compiles them on the next start.

    Ren'Py's own tools/uninstall.py does the same job from the same manifest if
    you would rather not run PowerShell.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File uninstall.ps1 "D:\Games\CityDevilRestart-0.4.0-pc"
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

# The installer records two lists and they answer two different questions.
#   files       every path the patch is answerable for
#   introduced  the subset that did not exist before and must be deleted
# A path with a backup is restored; a path without one is removed.
$manifestPath = Join-Path $backup "manifest.json"
$rels = @()
if (Test-Path -LiteralPath $manifestPath) {
    $m = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($m.files)       { $rels += @($m.files) }
    if ($m.introduced)  { $rels += @($m.introduced) }
}

if ($rels.Count -eq 0) {
    # Manifest missing or empty: fall back to whatever was backed up.
    Get-ChildItem -LiteralPath $backup -Recurse -File | ForEach-Object {
        if ($_.Name -eq "manifest.json") { return }
        $rels += ($_.FullName.Substring($backup.Length + 1) -replace '\\', '/')
    }
}

$restored = 0
$removed  = 0

foreach ($rel in ($rels | Sort-Object -Unique)) {
    $win = $rel -replace '/', '\'
    $src = Join-Path $backup $win
    $dst = Join-Path $game $win
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
}

# Recompiled bytecode belongs to whichever scripts are in place now, so it has
# to go either way: a .rpyc whose .rpy just changed, and one whose .rpy the
# patch has just deleted.
$k = 0
Get-ChildItem -LiteralPath $game -File -ErrorAction SilentlyContinue |
    Where-Object { $_.Extension -in ".rpyc", ".rpymc" } |
    ForEach-Object {
        $srcExt = if ($_.Extension -eq ".rpyc") { ".rpy" } else { ".rpym" }
        $base = [System.IO.Path]::ChangeExtension($_.FullName, $srcExt)
        # Its source is on disk, so it is the real bytecode for it -- which now
        # means the scripts the patch just put back, not the ones we installed.
        # Ren'Py recompiles it on the next start.
        if (Test-Path -LiteralPath $base) {
            Remove-Item -LiteralPath $_.FullName -Force
            $k++
        }
    }

# The caches install.ps1 dropped are rebuilt on the next start; nothing to undo.

Remove-Item -LiteralPath $backup -Recurse -Force

Write-Host ""
Write-Host "restored $restored file(s), removed $removed patch-only file(s), dropped $k recompiled .rpyc"
Write-Host "done -- the game is back to its original English state, and its scripts"
Write-Host "come out of archive.rpa again."

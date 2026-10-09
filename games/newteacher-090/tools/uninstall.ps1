<#
.SYNOPSIS
    Remove the That New Teacher 0.9.0 Simplified Chinese patch and put the game back.

.DESCRIPTION
    Puts back every file install.ps1 overwrote -- the 51 revised scripts and
    the compiled .rpyc set the download shipped alongside them -- and deletes
    everything it introduced, which is only the language shim.  What to restore
    and what to delete is read from the manifest the installer wrote, so it
    survives the patch tree being edited between install and uninstall.

    Afterwards game/tl/chinese/ is the download's own translation again, not
    the publisher's original for the 43 files this patch revised and the
    revised text for the rest.  Ren'Py recompiles bytecode on the next start.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File uninstall.ps1 "D:\Games\That_New_Teacher"
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

# The installer records three lists.
#   files       every path the patch is answerable for
#   introduced  the subset that did not exist before and must be deleted
#   compiled    the .rpyc that were moved aside, restored from the backup
# A path with a backup is restored; a path without one is removed.
$manifestPath = Join-Path $backup "manifest.json"
$rels = @()
if (Test-Path -LiteralPath $manifestPath) {
    $m = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($m.files)      { $rels += @($m.files) }
    if ($m.compiled)   { $rels += @($m.compiled) }
    if ($m.introduced) { $rels += @($m.introduced) }
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

# Bytecode the game rebuilt while the patch was installed belongs to whichever
# scripts are in place now, so it has to go either way.  This sweep has to be
# recursive: unlike a game whose scripts sit at game/ root, this one's live in
# game/tl/chinese/ and its subdirectories.
$k = 0
Get-ChildItem -LiteralPath $game -Recurse -File -Include *.rpyc, *.rpymc -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -notlike "$backup*" } |
    ForEach-Object {
        $srcExt = if ($_.Extension -eq ".rpyc") { ".rpy" } else { ".rpym" }
        $base = [System.IO.Path]::ChangeExtension($_.FullName, $srcExt)
        # Its source is on disk, so it is the real bytecode for it -- which now
        # means the scripts just restored, not the ones the patch installed.
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
Write-Host "done -- game/tl/chinese/ is back to what the download shipped."

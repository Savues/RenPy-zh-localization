<#
.SYNOPSIS
    Remove the 60 Days Of Us 3.1.3 Simplified Chinese patch and put the game back.

.DESCRIPTION
    Restores game/archive.rpa from the backup the installer took, which returns it
    to its original length exactly -- the surgery only ever appended an index, so
    putting the original file back is sufficient and is the only safe way to undo
    it. Then it puts back every translation file the patch overwrote and deletes
    the ones it introduced.

    After this the game is the download again: its own Chinese is back inside the
    archive and game/tl/Chinese/ is gone.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File uninstall.ps1 "D:\Games\60DaysOfUs-Build3.1.3(EarlyAccess)-pc"
#>
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$GameDir
)

$ErrorActionPreference = "Stop"

$gameDir = $GameDir.TrimEnd('')
if (Test-Path -LiteralPath (Join-Path $gameDir "game")) {
    $game = Join-Path $gameDir "game"
} elseif ((Split-Path -Leaf $gameDir) -eq "game") {
    $game = $gameDir
} else {
    Write-Error "not a Ren`Py game directory (no game/ inside): $gameDir"
}

$backup = Join-Path $game ".zh_patch_backup"
if (-not (Test-Path -LiteralPath $backup)) {
    Write-Error "no backup at $backup -- install.ps1 was never run here."
}

# ---- 1) the archive --------------------------------------------------------
# Unconditional. If the backup is missing the archive cannot be trusted, because
# we cannot tell whether it has already been rewritten, and running the game on
# a half-patched archive is exactly the state this script exists to end.
$archive     = Join-Path $game "archive.rpa"
$archiveBak  = Join-Path $backup "archive.rpa"
if (-not (Test-Path -LiteralPath $archiveBak)) {
    Write-Error "no archive backup at $archiveBak."
    Write-Error "game/archive.rpa cannot be restored, so it may still be the patched copy."
    Write-Error "Restore it from your own copy of the download before launching the game."
    exit 1
}

$before = (Get-Item -LiteralPath $archive).Length
Copy-Item -LiteralPath $archiveBak -Destination $archive -Force
$after = (Get-Item -LiteralPath $archive).Length
Write-Host ("  archive.rpa  {0:N0} -> {1:N0} bytes (original length)" -f $before, $after)

# ---- 2) the translation tree and the shim ----------------------------------
$rels = @()
$manifestPath = Join-Path $backup "manifest.json"
if (Test-Path -LiteralPath $manifestPath) {
    $m = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($m.files)      { $rels += @($m.files) }
    if ($m.compiled)   { $rels += @($m.compiled) }
    if ($m.introduced) { $rels += @($m.introduced) }
}
if ($rels.Count -eq 0) {
    Get-ChildItem -LiteralPath $backup -Recurse -File | ForEach-Object {
        if ($_.Name -eq "manifest.json") { return }
        if ($_.Name -eq "archive.rpa") { return }
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
    } elseif (Test-Path -LiteralPath $dst) {
        Remove-Item -LiteralPath $dst -Force
        $removed++
    }
}

# Bytecode the game rebuilt while the patch was installed belongs to whichever
# scripts are in place now. This sweep has to be recursive: the translation
# lives in a subdirectory, not at game/ root.
$k = 0
Get-ChildItem -LiteralPath $game -Recurse -File -Include *.rpyc, *.rpymc -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -notlike "$backup*" } |
    ForEach-Object {
        $srcExt = if ($_.Extension -eq ".rpyc") { ".rpy" } else { ".rpym" }
        $base = [System.IO.Path]::ChangeExtension($_.FullName, $srcExt)
        if (Test-Path -LiteralPath $base) { Remove-Item -LiteralPath $_.FullName -Force; $k++ }
    }

# The tree is empty now that its files are gone; leave no empty shells behind.
$tl = Join-Path $game "tl\Chinese"
if (Test-Path -LiteralPath $tl) {
    if (-not (Get-ChildItem -LiteralPath $tl -Recurse -File)) {
        Remove-Item -LiteralPath $tl -Recurse -Force
        Write-Host "  removed   tl/Chinese (left empty by the patch)"
    }
}

Remove-Item -LiteralPath $backup -Recurse -Force

Write-Host ""
Write-Host "restored $restored file(s), removed $removed patch-only file(s), dropped $k recompiled .rpyc"
Write-Host "done -- archive.rpa is the original again and the game`s own Chinese is back inside it."

<#
.SYNOPSIS
    install/uninstall round-trip on a fixture, not on a real installation.

.DESCRIPTION
    Resets tmp_fixture\game from the pristine English scripts plus the published
    mod, runs tools\install.ps1 -WithMod, runs tools\uninstall.ps1, then compares
    every file against a SHA-256 snapshot taken beforehand.

    The fixture is not in the repository -- it needs the game's own renpy\ and
    lib\python3.9 for the bundled interpreter to start, plus the English release
    scripts this repository deliberately does not redistribute.  Build it once:

      fixture\
        pristine\scripts\         the 19 English .rpy and their .rpyc
        pristine\mod\             the published Shawn's Mod
        renpy\                    copied from a game install
        lib\py3-windows-x86_64\   copied from a game install
        lib\python3.9\            copied from a game install

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File tools\roundtrip_test.ps1 -Fixture D:\tmp\fixture
#>
param(
    [Parameter(Mandatory = $true)]
    [string]$Fixture
)

$ErrorActionPreference = "Stop"
$here      = Split-Path -Parent $MyInvocation.MyCommand.Path
$install   = Join-Path $here "install.ps1"
$uninstall = Join-Path $here "uninstall.ps1"
$game      = Join-Path $Fixture "game"

if (-not (Test-Path -LiteralPath (Join-Path $Fixture "renpy")) -or
    -not (Test-Path -LiteralPath (Join-Path $Fixture "pristine\scripts"))) {
    Write-Error "fixture is incomplete -- see .DESCRIPTION for what it needs: $Fixture"
}

function Reset-Game {
    if (Test-Path -LiteralPath $game) { Remove-Item -LiteralPath $game -Recurse -Force }
    New-Item -ItemType Directory -Force -Path $game | Out-Null
    # -Path, not -LiteralPath: only -Path expands the wildcard.
    Copy-Item -Path (Join-Path $Fixture "pristine\scripts\*") -Destination $game -Force
    Copy-Item -LiteralPath (Join-Path $Fixture "pristine\mod") -Destination (Join-Path $game "mod") -Recurse -Force
}

function Snapshot([string]$out) {
    Get-ChildItem -LiteralPath $Fixture -Recurse -File |
        Where-Object { $_.Name -notin "before.txt", "after.txt" } |
        ForEach-Object {
            "{0}  {1}" -f (Get-FileHash $_.FullName -Algorithm SHA256).Hash.Substring(0, 16),
                          $_.FullName.Substring($Fixture.Length + 1)
        } |
        Sort-Object { $_.Substring(17) } |
        Set-Content -LiteralPath $out -Encoding UTF8
}

# The two snapshots live inside the fixture, so a leftover after.txt from
# an earlier run would be in the "before" list and then change underneath it.
foreach ($n in "before.txt", "after.txt") {
    Remove-Item -LiteralPath (Join-Path $Fixture $n) -Force -ErrorAction SilentlyContinue
}

Reset-Game
Snapshot (Join-Path $Fixture "before.txt")
$count = (Get-Content (Join-Path $Fixture "before.txt")).Count
Write-Host "fixture: $Fixture ($count files)"

Write-Host ""
Write-Host "--- install -WithMod"
& $install $Fixture -WithMod
if ($LASTEXITCODE -ne 0) { throw "install.ps1 exited $LASTEXITCODE" }

$rpy   = (Get-ChildItem $game -Filter *.rpy -File).Count
$mods  = (Get-ChildItem (Join-Path $game "mod") -Filter *.rpyc -File).Count
$fonts = (Get-ChildItem (Join-Path $game "Fonts") -ErrorAction SilentlyContinue).Count
$shim  = Test-Path (Join-Path $game "000_zh_fonts.rpy")
$stale = (Get-ChildItem $game -Filter *.rpyc -File).Count
Write-Host "  installed $rpy .rpy, $mods mod .rpyc, $fonts fonts, shim=$shim, stale bytecode=$stale"
if ($stale -ne 0) { throw "$stale stale .rpyc survived install" }

Write-Host ""
Write-Host "--- uninstall"
& $uninstall $Fixture
if ($LASTEXITCODE -ne 0) { throw "uninstall.ps1 exited $LASTEXITCODE" }

Snapshot (Join-Path $Fixture "after.txt")
$diff = Compare-Object (Get-Content (Join-Path $Fixture "before.txt")) (Get-Content (Join-Path $Fixture "after.txt"))
if ($diff) {
    Write-Host ""
    Write-Host "DIFFS ($($diff.Count)):"
    $diff | ForEach-Object { "  " + $_.SideIndicator + " " + $_.InputObject }
    exit 1
}

Write-Host ""
Write-Host "round trip clean: $count files byte-identical to the pre-install state"

<#
.SYNOPSIS
    Install the Wartribe Academy 2.0.3 Simplified Chinese patch.

.DESCRIPTION
    Wartribe Academy does not use Ren'Py translations.  It ships no
    game/tl/<lang>/ templates, only game/tl/None/common.rpym, so there is no
    translate tree to drop into game/tl/ -- the scripts themselves are the patch.

    This replaces 15 of the game's own .rpy files with Chinese ones, drops the
    font shim, and installs three faces under game/fonts/.  Anything it
    overwrites is copied to game/.zh_patch_backup/ the first time it is touched.
    Run tools/uninstall.ps1 to put the game back exactly as it was.

    No Python required.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 "D:\Games\WartribeAcademy-2.0.3-pc"
#>
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$GameDir
)

$ErrorActionPreference = "Stop"

$here    = Split-Path -Parent $MyInvocation.MyCommand.Path
$gameDir = $GameDir.TrimEnd('\')
$repoDir = Split-Path -Parent $here          # .../games/wartribeacademy-0203

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

$manifest_ = Get-Content -LiteralPath (Join-Path $repoDir "game.json") -Raw -Encoding UTF8 | ConvertFrom-Json
if ($manifest_.patch_layout -ne "script-override") {
    Write-Error "game.json says patch_layout=$($manifest_.patch_layout); this installer only handles script-override."
    exit 1
}

$backup = Join-Path $game ".zh_patch_backup"
$patchGame = Join-Path $repoDir "patch\game"
$shimRel   = $manifest_.shim
$shimSrc   = Join-Path $repoDir "patch\$shimRel"
$fontSrc   = Join-Path $repoDir "assets\fonts"
$touched   = New-Object System.Collections.Generic.List[string]
$introduced = New-Object System.Collections.Generic.List[string]

function Backup-Once([string]$rel) {
    $src = Join-Path $game $rel
    $dst = Join-Path $backup $rel
    if (Test-Path -LiteralPath $dst) { return $false }   # first touch only
    # Nothing to do when the file did not exist: tools/uninstall.py reads the
    # absence of a backup entry as "the patch introduced this file, delete it
    # again on uninstall". Leaving no placeholder keeps the backup directory
    # free of empty scaffolding, same convention as tools/install.py.
    if (-not (Test-Path -LiteralPath $src)) { return $false }
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
    if ((Get-Item -LiteralPath $src).PSIsContainer) {
        Copy-Item -LiteralPath $src -Destination $dst -Recurse -Force
    } else {
        Copy-Item -LiteralPath $src -Destination $dst -Force
    }
    return $true
}

function Place([string]$rel, [string]$srcFile) {
    if (Backup-Once $rel) { } else {
        if (-not (Test-Path -LiteralPath (Join-Path $game $rel))) {
            $introduced.Add($rel)
        }
    }
    $dst = Join-Path $game $rel
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
    Copy-Item -LiteralPath $srcFile -Destination $dst -Force
    $touched.Add($rel)
}

Write-Host "Wartribe Academy 2.0.3 [schinese] -> $game"

# ---- 1) translated scripts -------------------------------------------------
$n = 0
Get-ChildItem -LiteralPath $patchGame -Recurse -File -Filter *.rpy | ForEach-Object {
    $rel = $_.FullName.Substring($patchGame.Length + 1)
    Place $rel $_.FullName
    $n++
}
Write-Host ("  scripts            {0,3} files" -f $n)

# ---- 2) font shim ----------------------------------------------------------
Place $shimRel $shimSrc
Write-Host "  shim               $shimRel"

# ---- 3) CJK fonts ----------------------------------------------------------
$fonts = 0
foreach ($fa in $manifest_.font_assets) {
    $srcFace = Join-Path $repoDir ($fa.path -replace '/', '\')
    if (-not (Test-Path -LiteralPath $srcFace)) {
        Write-Error "font asset missing: $($fa.path)"
        exit 1
    }
    foreach ($name in $fa.names) {
        Place "fonts/$name" $srcFace
        $fonts++
    }
}
Write-Host ("  fonts              {0,2} files" -f $fonts)

# ---- 4) drop stale bytecode ------------------------------------------------
# Ren'Py prefers .rpyc; a stale one silently wins over the .rpy we just wrote,
# and the player then sees an English game with no error anywhere.
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
# "files" is the list tools/uninstall.py reads, so either installer can be
# undone with either uninstaller.
@{
    version    = 2
    game       = "wartribeacademy-0203"
    lang       = $manifest_.language
    scripts    = $n
    shim       = $shimRel
    fonts      = @($manifest_.font_assets | ForEach-Object { $_.names } | ForEach-Object { $_ })
    introduced = @($introduced | Sort-Object)
    files      = @($touched | Sort-Object)
} | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $backup "manifest.json") -Encoding UTF8

Write-Host ""
Write-Host "done. launch the game -- the Chinese scripts are compiled on first start."
Write-Host ""
Write-Host "to undo:  powershell -NoProfile -ExecutionPolicy Bypass -File `"$here\uninstall.ps1`" `"$gameDir`""
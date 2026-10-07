<#
.SYNOPSIS
    Install the DropOut Saga 0.12.0b Simplified Chinese patch.

.DESCRIPTION
    DropOut Saga does not use Ren'Py translations.  The release ships only
    game/tl/None/common.rpym -- no per-language templates -- so this patch replaces
    19 of the game's own .rpy files with Chinese ones, and the scripts themselves
    are the patch.  Five more scripts are additions: the compatibility shim, the
    guide tool, its two data tables and the toolbox.

    Anything it overwrites is copied to game/.zh_patch_backup/ the first time it
    is touched.  Run tools/uninstall.ps1 to put the game back exactly as it was.

    -WithMod additionally translates Shawn's Mod.  The mod is third-party and is
    not redistributed here: the tool reads whatever .rpyc the player has in
    game/mod and rewrites a copy, using the interpreter inside the game.  That
    interpreter is mandatory -- see tools/mod_translate.py for why a normal
    Python produces a file the engine silently refuses to load.

    No Python required for the base patch.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 "D:\Games\DropOutSaga-0.12.0b-pc"

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 "D:\Games\DropOutSaga-0.12.0b-pc" -WithMod
#>
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$GameDir,

    [switch]$WithMod
)

$ErrorActionPreference = "Stop"

$here    = Split-Path -Parent $MyInvocation.MyCommand.Path
$gameDir = $GameDir.TrimEnd('\')
$repoDir = Split-Path -Parent $here          # .../games/dropout-saga-0120

# ---- locate the game -------------------------------------------------------
if (Test-Path -LiteralPath (Join-Path $gameDir "game")) {
    $game = Join-Path $gameDir "game"
} elseif ((Split-Path -Leaf $gameDir) -eq "game") {
    $game = $gameDir
} else {
    Write-Error "not a Ren'Py game directory (no game/ inside): $gameDir"
}
if (-not (Test-Path -LiteralPath (Join-Path $game "script.rpy")) -and
    -not (Test-Path -LiteralPath (Join-Path $game "script.rpyc"))) {
    Write-Error "no script.rpy in $game -- is this really the game directory?"
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

function Backup-Once([string]$rel) {
    $src = Join-Path $game $rel
    $dst = Join-Path $backup $rel
    if (Test-Path -LiteralPath $dst) { return $false }   # first touch only
    # Nothing to do when the file did not exist: tools/uninstall.ps1 reads the
    # absence of a backup entry as "the patch introduced this file, delete it
    # again on uninstall".
    if (-not (Test-Path -LiteralPath $src)) { return $false }
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
    if ((Get-Item -LiteralPath $src).PSIsContainer) {
        Copy-Item -LiteralPath $src -Destination $dst -Recurse -Force
    } else {
        Copy-Item -LiteralPath $src -Destination $dst -Force
    }
    return $true
}

function Drop-StaleBytecode {
    # Ren'Py prefers .rpyc; a stale one silently wins over the .rpy just written.
    # Only bytecode with a matching source is dropped -- game/mod/*.rpyc ships
    # with no .rpy sibling and has to survive.  The backup tree is skipped
    # explicitly: this loop backs files up as it goes, and a fresh
    # .zh_patch_backup copy is itself a .rpyc sitting next to a .rpy, so an
    # unfiltered -Recurse deletes the backup it just made and counts it too.
    # That is how 19 files turned into "removed bytecode 33".
    $k = 0
    Get-ChildItem -LiteralPath $game -Recurse -File |
        Where-Object { $_.Extension -in ".rpyc", ".rpymc" } |
        Where-Object { -not $_.FullName.StartsWith($backup + "\") } |
        ForEach-Object {
        $srcExt = if ($_.Extension -eq ".rpyc") { ".rpy" } else { ".rpym" }
        $base = [System.IO.Path]::ChangeExtension($_.FullName, $srcExt)
        if (Test-Path -LiteralPath $base) {
            # Back it up first.  The .rpyc is what the game would have run
            # before this patch existed, and uninstall.ps1 cannot put back a
            # file nobody saved.
            $rel = $_.FullName.Substring($game.Length + 1)
            if (Backup-Once $rel) { $touched.Add(($rel -replace '\\', '/')) }
            Remove-Item -LiteralPath $_.FullName -Force
            $k++
        }
    }
    return $k
}

Write-Host "DropOut Saga 0.12.0b [schinese] -> $game"

# ---- 1) translated scripts -------------------------------------------------
$n = 0
Get-ChildItem -LiteralPath $patchGame -Recurse -File -Filter *.rpy | ForEach-Object {
    $rel = $_.FullName.Substring($patchGame.Length + 1)
    Backup-Once $rel | Out-Null
    $dst = Join-Path $game $rel
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
    Copy-Item -LiteralPath $_.FullName -Destination $dst -Force
    $touched.Add(($rel -replace '\\', '/'))
    $n++
}
Write-Host ("  scripts            {0,3} files" -f $n)

# ---- 2) font shim ----------------------------------------------------------
Backup-Once $shimRel | Out-Null
Copy-Item -LiteralPath $shimSrc -Destination (Join-Path $game $shimRel) -Force
$touched.Add($shimRel)
Write-Host "  shim               $shimRel"

# ---- 3) CJK font -----------------------------------------------------------
$fonts = 0
foreach ($fa in $manifest_.font_assets) {
    $srcFace = Join-Path $repoDir ($fa.path -replace '/', '\')
    foreach ($name in $fa.names) {
        $rel = "Fonts/$name"
        Backup-Once $rel | Out-Null
        New-Item -ItemType Directory -Force -Path (Join-Path $game "Fonts") | Out-Null
        Copy-Item -LiteralPath $srcFace -Destination (Join-Path $game "Fonts\$name") -Force
        $touched.Add($rel)
        $fonts++
    }
}
Write-Host ("  fonts              {0,2} files" -f $fonts)

# ---- 4) drop stale bytecode ------------------------------------------------
Write-Host ("  removed bytecode   {0,3} .rpyc/.rpymc" -f (Drop-StaleBytecode))

# ---- 5) optional: translate Shawn's Mod ------------------------------------
# The mod is rebuilt, never shipped.  See game.json _mod_translation for why:
# a .rpyc has no source to translate and the published builds differ.
$modFiles = 0
if ($WithMod) {
    $modDir = Join-Path $game "mod"
    if (-not (Test-Path -LiteralPath $modDir)) {
        Write-Error "-WithMod was given but there is no $modDir. Install Shawn's Mod into the game first, then re-run."
        exit 1
    }
    if (-not (Get-ChildItem -LiteralPath $modDir -Filter *.rpyc -File)) {
        Write-Error "$modDir holds no .rpyc -- the .rpyc-only release build is what this tool reads."
        exit 1
    }

    # The rewrite re-pickles AST nodes, and that pickle has to be one the engine
    # can read.  Ren'Py 8.3 runs Python 3.9, so use the interpreter it shipped.
    $py = @(Get-ChildItem -LiteralPath (Join-Path $gameDir "lib") -Directory -Filter "py3-*" |
            ForEach-Object { Join-Path $_.FullName "python.exe" } |
            Where-Object { Test-Path -LiteralPath $_ })
    if ($py.Count -eq 0) {
        Write-Error "no bundled interpreter under $gameDir\lib\py3-*\python.exe -- cannot rewrite .rpyc safely."
        exit 1
    }

    $build = Join-Path $game ".zh_mod_build"
    if (Test-Path -LiteralPath $build) { Remove-Item -LiteralPath $build -Recurse -Force }
    Write-Host ("  mod interpreter    {0}" -f $py[0])
    & $py[0] (Join-Path $here "mod_translate.py") $gameDir (Join-Path $repoDir "data\mod_zh.json") $build $modDir
    if ($LASTEXITCODE -ne 0) {
        Write-Error "mod_translate.py failed (exit $LASTEXITCODE); the game's own game\mod was not touched."
        exit 1
    }

    Get-ChildItem -LiteralPath $build -Filter *.rpyc -File | ForEach-Object {
        $rel = "mod/$($_.Name)"
        Backup-Once $rel | Out-Null
        Copy-Item -LiteralPath $_.FullName -Destination (Join-Path $game $rel) -Force
        $touched.Add($rel)
        $modFiles++
    }
    Remove-Item -LiteralPath $build -Recurse -Force
    Write-Host ("  mod                {0,3} .rpyc rebuilt" -f $modFiles)
} elseif (Test-Path -LiteralPath (Join-Path $game "mod")) {
    Write-Host "  mod                not translated (re-run with -WithMod)"
}

# ---- 6) record what we did -------------------------------------------------
# "files" is the same list tools/uninstall.ps1 reads, so the manifest documents
# the install rather than driving it; the backup directory is what actually
# gets walked back.
@{
    version   = 2
    game      = "dropout-saga-0120"
    lang      = $manifest_.language
    scripts   = $n
    shim      = $shimRel
    fonts     = $fonts
    mod_files = $modFiles
    files     = @($touched | Sort-Object)
} | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $backup "manifest.json") -Encoding UTF8

Write-Host ""
Write-Host "done. launch the game -- the Chinese scripts are compiled on first start."
if ($modFiles -eq 0) {
    Write-Host "if you use Shawn's Mod, uninstall it, re-run this with -WithMod, then install the mod again."
}
Write-Host ""
Write-Host "to undo:  powershell -NoProfile -ExecutionPolicy Bypass -File `"$here\uninstall.ps1`" $gameDir"

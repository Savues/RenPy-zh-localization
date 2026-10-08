@echo off
rem =====================================================================
rem  DropOut Saga - translate Shawn's Mod into Chinese.
rem
rem  MUST be run with the interpreter that ships inside the game.  Rebuilding
rem  the .rpyc means re-pickling Ren'Py AST nodes, and that pickle has to be
rem  one the engine can read: this game is Ren'Py 8.3 on Python 3.9, and a
rem  .rpyc written by any newer interpreter is silently skipped by the
rem  engine -- renpy/script.py wraps the load in "except Exception: pass"
rem  and you only get "Could not load file ...rpyc".
rem
rem  Usage:  drag the game's .exe onto this file, or paste the game folder.
rem =====================================================================
chcp 65001 >nul
setlocal DisableDelayedExpansion

set "GAME=%~1"
if "%GAME%"=="" set /p "GAME=游戏所在文件夹的完整路径: "
if "%GAME%"=="" (echo 没有给出路径，退出。 & pause & exit /b 1)

rem Accept the game folder, a dragged .exe, or a path pointing at game\.
rem A pasted path often carries a doubled separator or a trailing \, and both
rem are cleared first because every check below is a path test.
set "GAME=%GAME:\\=\%"
if "%GAME:~-1%"=="\" set "GAME=%GAME:~0,-1%"
if not exist "%GAME%\" for %%F in ("%GAME%") do set "GAME=%%~dpF"
set "GAME=%GAME:\\=\%"
if "%GAME:~-1%"=="\" set "GAME=%GAME:~0,-1%"
if /i "%GAME:~-5%"=="\game" set "GAME=%GAME:~0,-5%"
if not exist "%GAME%\game\" (
    echo 这不是游戏目录（里面没有 game\）：%GAME%
    pause
    exit /b 1
)

set "MOD=%GAME%\game\mod"
if not exist "%MOD%\" (
    echo 找不到 %MOD%
    echo 先把 Shawn's Mod 装进游戏，再运行本脚本。
    pause
    exit /b 1
)

set "PY="
for /d %%D in ("%GAME%\lib\py3-*") do if exist "%%D\python.exe" set "PY=%%D\python.exe"
if "%PY%"=="" (
    echo 找不到游戏自带的解释器：%GAME%\lib\py3-*\python.exe
    pause
    exit /b 1
)

set "OUT=%GAME%\.zh_mod_build"
echo 解释器  %PY%
echo MOD      %MOD%
echo 输出     %OUT%
echo.

if exist "%OUT%\" rmdir /s /q "%OUT%"
"%PY%" "%~dp0mod_translate.py" "%GAME%" "%~dp0mod_zh.json" "%OUT%"
if errorlevel 1 (
    echo.
    echo 重建失败。游戏里的 MOD 没有被动过。
    pause
    exit /b 1
)

set /a N=0
for %%F in ("%OUT%\*.rpyc") do (
    copy /y "%%~fF" "%MOD%\%%~nxF" >nul || goto :failed
    set /a N+=1
)
if "%N%"=="0" goto :failed
rmdir /s /q "%OUT%"
echo.
echo 完成。%MOD% 里的 %N% 个 .rpyc 已换成中文版。
goto :done

:failed
echo 没有可复制的文件，游戏里的 MOD 可能处于半更新状态。重新运行本脚本即可。
pause
exit /b 1

:done
echo 启动游戏看看。MOD 界面和攻略现在应该是中文。
pause

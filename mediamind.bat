@echo off
REM MediaMind - Windows批处理版本

setlocal enabledelayedexpansion

REM 设置颜色代码
for /f "tokens=4 delims=[]" %%a in ('prompt $H^&echo on & for %%b in (1) do rem') do set "BLACK=%%a"
for /f "tokens=2 delims=#" %%a in ('prompt $E# & echo.^&prompt $E') do set "ANSI=%%a"

set "RED=%ANSI%[91m"
set "GREEN=%ANSI%[92m"
set "YELLOW=%ANSI%[93m"
set "BLUE=%ANSI%[94m"
set "NC=%ANSI%[0m"

REM 默认值
set "DIRECTORY="
set "SCAN_ONLY=false"
set "VERBOSE=false"

REM 解析参数
:loop
if "%~1"=="" goto :main
if /i "%~1"=="-h" goto :show_help
if /i "%~1"=="--help" goto :show_help
if /i "%~1"=="--scan-only" (
    set "SCAN_ONLY=true"
    shift
    goto :loop
)
if /i "%~1"=="-v" (
    set "VERBOSE=true"
    shift
    goto :loop
)
if /i "%~1"=="--verbose" (
    set "VERBOSE=true"
    shift
    goto :loop
)
if "%DIRECTORY%"=="" (
    set "DIRECTORY=%~1"
    shift
    goto :loop
)

echo %RED%错误: 多余的参数: %1%NC%
exit /b 1

:show_help
echo MediaMind - 媒体智能管家
echo.
echo 用法: %~n0 ^<目录^> [选项]
echo.
echo 参数:
echo     ^<目录^>     媒体文件目录（必需）
echo.
echo 选项:
echo     -h, --help     显示此帮助信息
echo     --scan-only    只扫描，不整理
echo     -v, --verbose  详细输出
echo.
echo 示例:
echo     %~n0 v:/media/drama          # 整理电视剧
echo     %~n0 v:/media --scan-only   # 只扫描
echo     %~n0 v:/media -v            # 详细输出
echo.
echo MediaMind会自动检测变化并只整理需要的内容！
exit /b 0

:check_python
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo %RED%错误: 未找到Python%NC%
    echo %YELLOW%请安装Python 3.6或更高版本%NC%
    exit /b 1
)
goto :eof

:check_directory
if not exist "%~1" (
    echo %RED%错误: 目录不存在: %~1%NC%
    exit /b 1
)
goto :eof

:run_mind
set directory=%1
set scan_only=%2
set verbose=%3

set "python_script=%~dp0mediamind.py"
if not exist "%python_script%" (
    echo %RED%错误: 找不到mediamind.py脚本%NC%
    exit /b 1
)

set "cmd=python "%python_script%" "%directory%""

if "%scan_only%"=="true" (
    set "cmd=!cmd! --scan-only"
)

if "%verbose%"=="true" (
    echo %BLUE%正在执行: !cmd!%NC%
    python "%python_script%" "%directory%" --scan-only
) else (
    python "%python_script%" "%directory%"
)
goto :eof

:main
if "%DIRECTORY%"=="" (
    echo %RED%错误: 请指定媒体目录%NC%
    goto :show_help
)

echo %BLUE%🎬 MediaMind - 媒体智能管家%NC%
echo %BLUE%=================================%NC%
echo.

call :check_python
call :check_directory "%DIRECTORY%"
call :run_mind "%DIRECTORY%" "%SCAN_ONLY%" "%VERBOSE%"

echo.
echo %GREEN%✨ MediaMind 完成！%NC%
endlocal
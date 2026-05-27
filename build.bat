@echo off
chcp 65001 >nul
echo ========================================
echo YGP工具箱 EXE打包脚本
echo ========================================
echo.

echo [1/3] 检查Python环境...
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请先安装Python
    pause
    exit /b 1
)

echo [2/3] 安装依赖包...
pip install pywebview pyinstaller -q
if errorlevel 1 (
    echo 错误: 依赖安装失败
    pause
    exit /b 1
)

echo [3/3] 开始打包EXE文件...
pyinstaller ygp-tools.spec --clean
if errorlevel 1 (
    echo 错误: 打包失败
    pause
    exit /b 1
)

echo.
echo ========================================
echo 打包完成！
echo 输出文件: dist\YGP工具箱.exe
echo ========================================
pause

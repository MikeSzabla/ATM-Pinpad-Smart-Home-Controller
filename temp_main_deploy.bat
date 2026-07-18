@echo off
set PORT=COM3

echo.
echo ================================
echo Deploying temp_main to ESP32...
echo ================================

mpremote connect %PORT% fs cp .\src\temp_main.py        :main.py

echo.
echo Soft resetting ESP32...
mpremote connect %PORT% soft-reset

echo.
echo Deployment complete.
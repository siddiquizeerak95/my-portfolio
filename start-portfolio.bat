@echo off
title Zeerak Shafique - Digital Afterdark Portfolio
echo ========================================================
echo   ZEERAK SHAFIQUE // DIGITAL AFTERDARK PORTFOLIO
echo   Role: BCA Student & Aspiring Creative Developer
echo   Server: http://localhost:8080/index.html
echo ========================================================
echo.
echo Launching browser and starting local web server...
start "" http://localhost:8080/index.html
python -m http.server 8080
pause

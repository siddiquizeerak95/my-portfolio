@echo off
title Zeerak Shafique - Digital World Portfolio // Aspiring Full-Stack Developer
echo ========================================================
echo   ZEERAK SHAFIQUE // DIGITAL WORLD PORTFOLIO
echo   Role: BCA Student ^& Aspiring Full-Stack Developer
echo   Server: http://localhost:8080/index.html
echo ========================================================
echo.
echo Launching browser and starting local web server...
start "" http://localhost:8080/index.html
python -m http.server 8080
pause

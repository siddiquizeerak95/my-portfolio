@echo off
title ZEERAK — Zeerak Siddiqui | 3D Hybrid Creative Developer Portfolio
echo ========================================================
echo   ZEERAK // 3D HYBRID CREATIVE DEVELOPER PORTFOLIO
echo   Role: BCA Student ^& Creative Developer
echo   Server: http://localhost:8080/index.html
echo ========================================================
echo.
echo Launching browser and starting local web server...
start "" http://localhost:8080/index.html
python -m http.server 8080
pause

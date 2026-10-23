@echo off
title Zeerak Shafique - Obsidian Gold Portfolio // The Digital Atelier
echo ========================================================
echo   ZEERAK SHAFIQUE // OBSIDIAN GOLD PORTFOLIO
echo   The Digital Atelier - Luxury Creative Web Experience
echo   Role: BCA Student ^& Aspiring Creative Developer
echo   Server: http://localhost:8080/index.html
echo ========================================================
echo.
echo Launching browser and starting local web server...
start "" http://localhost:8080/index.html
python -m http.server 8080
pause

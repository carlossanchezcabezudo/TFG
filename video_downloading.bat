@echo off
echo =============================
echo   DESCARGADOR MASIVO YT-DLP
echo =============================

:: Cambiar al escritorio
cd /d "%USERPROFILE%\Desktop"

:: Instalar yt-dlp si no está
python -m pip install -U yt-dlp

:: Crear carpeta de salida
set "CARPETA_SALIDA=VideosDescargados"
if not exist "%CARPETA_SALIDA%" mkdir "%CARPETA_SALIDA%"

:: Ejecutar yt-dlp desde Python directamente
python -m yt_dlp -a urls.txt --recode-video mp4 -P "%CARPETA_SALIDA%"

echo -----------------------------
echo Descarga finalizada. Los vídeos están en: %CARPETA_SALIDA%
pause

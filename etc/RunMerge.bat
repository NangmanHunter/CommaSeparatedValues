@echo off
REM Python 스크립트 실행
python "C:\github-nangmanhunter\YoutubeShorts\etc\YouTube\Csv\etc\YouTubeURLCsv.py"

REM Python 종료 후 PS 스크립트 실행
powershell -ExecutionPolicy Bypass -File "C:\github-nangmanhunter\YoutubeShorts\etc\YouTube\Csv\etc\MergeFile.ps1"

pause
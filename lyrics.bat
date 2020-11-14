@echo off
cd C:/Users/Oromidayo/Music/
:loop
set /p lyrics="lyrics? "
IF "%lyrics%"=="" (exit) ELSE (youtube-dl  -f m4a "ytsearch:%lyrics%")
goto :loop

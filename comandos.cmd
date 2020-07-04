@echo off

cd C:\Users\blasc\PycharmProjects\auto_create_lib_repo_windows
python crear_repo.py %1

cd C:\Users\blasc\PycharmProjects\%1
git init
git remote add origin https://github.com/javibg96/%1.git
fsutil file createnew README2.md 0
fsutil file createnew requirements.txt 0
python C:\Users\blasc\PycharmProjects\auto_create_lib_repo_windows\rellenar_lib.py %1
git add .
git commit -m "Commit inicial"
git push -u origin master

start "" "C:\Program Files\JetBrains\PyCharm Community Edition 2020.1.1\bin\pycharm64.exe"
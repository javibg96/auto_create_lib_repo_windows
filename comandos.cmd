@echo off

cd C:\Users\blasc\PycharmProjects\auto_create_lib_repo_windows
python crear_repo.py %1

cd C:\Users\blasc\PycharmProjects\auto_create_lib_repo_windows\%1
git init
git remote add origin git@github.com:javibg96//$1.git
touch README.md
git add .
git commit -m "Initial commit"
git push -u origin master

start "" "C:\Program Files\JetBrains\PyCharm Community Edition 2020.1.1\bin\pycharm64.exe"
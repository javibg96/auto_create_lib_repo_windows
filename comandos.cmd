@echo off

cd C:\Users\blasc\PycharmProjects\auto_create_lib_repo_windows
python crear_repo.py %1
cd ..
mkdir %1
cd %1
git init
git remote add origin https://github.com/javibg96/%1.git
fsutil file createnew README.md 0
fsutil file createnew requirements.txt 0
mkdir src
cd src
fsutil file createnew version.py 0
cd C:\Users\blasc\PycharmProjects\auto_create_lib_repo_windows
python rellenar_lib.py %1

cd C:\Users\blasc\PycharmProjects\%1
git add .
git commit -m "Commit inicial"
git push -u origin master

start "" "C:\Program Files\JetBrains\PyCharm Community Edition 2020.1.1\bin\pycharm64.exe"
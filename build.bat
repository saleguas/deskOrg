del %cd%\output\dcmd.exe
pyinstaller --onefile dcmd.py
rd /s /q __pycache__
if exist __pycache__ rd /s /q __pycache__
rd /s /q build
if exist build rd /s /q build
MOVE %cd%\dist\dcmd.exe %cd%
rmdir dist /Q
del dcmd.spec
pause
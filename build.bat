pyinstaller --onefile main.py
rd /s /q __pycache__
if exist __pycache__ rd /s /q __pycache__
rd /s /q build
if exist build rd /s /q build
MOVE C:\Users\drale\Documents\desktoporganizer\dist\main.exe C:\Users\drale\Documents\desktoporganizer
rmdir dist /Q
del main.spec
pause
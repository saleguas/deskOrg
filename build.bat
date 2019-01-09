pyinstaller --onefile runner.py
rd /s /q __pycache__
if exist __pycache__ rd /s /q __pycache__
rd /s /q build
if exist build rd /s /q build
MOVE %cd%\dist\runner.exe %cd%
rmdir dist /Q
del runner.spec
pause
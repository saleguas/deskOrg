del %cd%\output\runner.exe
del %cd%\output\dcmd.exe

pyinstaller --onefile dcmd.py
rd /s /q __pycache__
if exist __pycache__ rd /s /q __pycache__
rd /s /q build
if exist build rd /s /q build
MOVE %cd%\dist\dcmd.exe %cd%
rmdir dist /Q
del dcmd.spec
pyinstaller --onefile runner.py
rd /s /q build
if exist build rd /s /q build
MOVE %cd%\dist\runner.exe %cd%
rmdir dist /Q
del runner.spec
if exist .idea rd /s /q .idea
if exist __pycache__ rd /s /q __pycache__
if not exist "output" mkdir "output"
MOVE %cd%\runner.exe %cd%\output
MOVE %cd%\dcmd.exe %cd%\output
pause
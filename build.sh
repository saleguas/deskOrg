#!/bin/bash

pyinstaller --onefile main.py
rm -r __pycache__
rm -r build
mv dist/main ./main_linux
rm -r dist
bzip2 main_linux
rm main.spec

#!/bin/bash

pyinstaller --onefile runner.py
rm -r __pycache__
rm -r build
mv dist/runner ./runner_linux
rm -r dist
bzip2 runner_linux
rm runner.spec

#!/bin/bash

pyinstaller --onefile runner.py
rm -r __pycache__
rm -r build
mv dist/runner ./runner_linux
rm -r dist
bzip2 runner_linux
rm runner.spec
pyinstaller --onefile dcmd.py
rm -R __pycache__
rm -R build
mv dist/dcmd ./dcmd_linux
rm -r dist
bzip2 dcmd_linux
rm runner.spec

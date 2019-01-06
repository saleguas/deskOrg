#!/bin/bash

python setup_linux.py build
tar -cf build_linux.tar build/
bzip2 build_linux.tar
rm -R build/

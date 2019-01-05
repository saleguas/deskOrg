#!/bin/bash

python setup.py build
tar -cf build.tar build/
bzip2 build.tar
rm -R build/

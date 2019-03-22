------------------------------------------------------------------------

# :file_folder: &nbsp; DesktopOrg &nbsp; :file_folder:

[![HitCount](http://hits.dwyl.io/saleguas/desktoporganizer.svg)](http://hits.dwyl.io/saleguas/desktoporganizer) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

#### DISCLAIMER:
I am ***NOT*** responsible for any problems it may cause, they should not appear in the first place though. 
Use at your own risk.

------------------------------------------------------------------------

## Introduction

Has your desktop ever looked like this?

![alt text](https://lureofmac.com/wp-content/uploads/2013/12/for-a-faster-mac.jpg)

![alt text](http://gcpcafe.com/wp-content/uploads/2013/05/cluttered-dessktop.jpg?w=300)

Then good news! I made this tool *specifically* for fixing issues like this and cluttered desktops. This python3 application will sort your files into folders based on a given input and clean up your desktop.

## Installation requirements

```diff
+ tqdm == 4.30.0
+ python3
+ Access to a terminal/shell/cmd
```
## Usage

If you want the help output, then here you go:
```bash
usage: dcmd.py [-h] [--extension] [--extract] [--backup] [--date DATE]
               [--name NAME] [--ascending ASCENDING]
               data_dir

Sorts files based on their attributes

positional arguments:
  data_dir              Path to the data directory

optional arguments:
  -h, --help            show this help message and exit
  --extension, -e       Sort files based on extension
  --extract, -x         Uproot all files to the current directory.
  --backup, -b          Backup files before any operation. Errors should not
                        happen but sometimes they do.
  --date DATE, -d DATE  Sort based on date modified. Use: D for Day, M for
                        Month, and Y for year.
  --ascending ASCENDING, -sba ASCENDING
                        Sort by ascending. Type * for precision. EX: *** would
                        sort by three letters

```

#### However if you still don't understand it, fret not!
#### 1. Simply open up a terminal
![alt text](https://github.com/saleguas/desktoporganizer/blob/master/images/opencmd.gif)

#### 2. Then run the dcmd.exe or dcmd.py file from the shell with the directory immediately following and any switches.
![alt text](https://github.com/saleguas/desktoporganizer/blob/master/images/go.gif)

Then you should have all your files nice and tidy.

If you don't like the outcome, you can reverse it by adding the -x switch or --extract. It moves all files up to the current folder. BE CAREFUL USING IT! If you were to use it on something such as your system32 folder, it would destroy your computer.






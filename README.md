# desktoporganizer
As the name implies, a desktop organizer that will move files into folders based on various attributes.

I am NOT responsible for any deletions/destruction/problems it may cause, they should not appear in the first place though. Use at your own risk.

[![HitCount](http://hits.dwyl.io/saleguas/desktoporganizer.svg)](http://hits.dwyl.io/saleguas/desktoporganizer) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 



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

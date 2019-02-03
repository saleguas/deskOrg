# desktoporganizer
As the name implies, a desktop organizer that will move files into folders based on various attributes.
The functionality and GUI is minimalistic for now which I plan to fix on future releases.

I am NOT responsible for any deletions/destruction/problems it may cause, they should not appear in the first place though. Use at your own risk.

[![HitCount](http://hits.dwyl.io/saleguas/desktoporganizer.svg)](http://hits.dwyl.io/saleguas/desktoporganizer)
```bash
usage: dcmd.exe [-h] [--extension] [--extract] [--backup] [--date DATE]
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
```
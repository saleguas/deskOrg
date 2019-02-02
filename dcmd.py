import argparse
from pathlib import Path
from modules import *


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')



parser = argparse.ArgumentParser(description='Sorts files based on their attributes')
parser.add_argument("data_dir",   type=lambda p: Path(p).absolute(),
        default=Path(__file__).absolute().parent / "data",
        help="Path to the data directory")
parser.add_argument("--extension", "-e",  dest='extension', action='store_true', help='Sort files based on extension')
parser.add_argument("--extract", "-x",  dest='extract', action='store_true', help='Uproot all files to the current directory.')
parser.add_argument("--backup", "-b",  dest='backup', action='store_true', help='Backup files before any operation. Errors should not happen but sometimes they do.')
parser.add_argument("--date", "-d",  dest='date',  help='Sort based on date modified. Use: D for Day, M for Month, and Y for year.')


args = parser.parse_args()

if(args.backup + args.extract + args.extension > 1):
    print("##########################################################")
    print("Using more than one switch can cause errors. Take caution.")
    print("##########################################################")
if(args.date):
    sortByDate(str(args.data_dir), str(args.date))
if(args.backup):
    backup(str(args.data_dir))
if(args.extract):
    extract(str(args.data_dir))
if(args.extension):
	sortByExtension(str(args.data_dir))

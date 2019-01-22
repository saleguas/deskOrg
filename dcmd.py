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
parser.add_argument("--name", "-n",  dest='name', action='store_true', help='Sort files based on name')
args = parser.parse_args()
if(args.name):
	sortByExtension(args.data_dir)
print(args.name)
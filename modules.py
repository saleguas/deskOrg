import os, glob
import shutil
import pathlib
import datetime
import re
from tqdm import tqdm

# I repeat a lot of code but it's hard to get around it.
# Sort by ascending order. The precision parameter shows how make characters it should sort to.
def sortByAscending(path, precision):
    logger = open(str(datetime.datetime.now()).replace(".", "-").replace(":", "-") + ".txt", 'w')
    for file in tqdm(os.listdir(path)):
        endPath = path + "/" + file
        ext = os.path.splitext(pathlib.Path(file))[0]
        if os.path.isfile(endPath):
            moved = False
            for dir in os.listdir(path):
                if os.path.isdir(path + "/" + dir):
                    if ext[0:len(precision)] == dir[0:len(precision)]:
                        moved = True
                        try:
                            shutil.move(endPath, path + "/" + dir)
                        except:
                            logger.write("Couldn't move " + endPath + " to " + (path + '/' + dir) + '\n')
                if not moved:
                    try:
                        os.mkdir(path + "/" + ext[0:len(precision)])
                        shutil.move(endPath, path + "/" + ext[0:len(precision)])
                    except:
                        logger.write("Couldn't move " + endPath + " to " + (path + '/' + dir) + '\n')
    logger.close()


# Sorts by extension of files.
def sortByExtension(path):
    logger = open("logs/" + str(datetime.datetime.now()).replace(':', '-').replace(".", '-') + ".txt", 'w')
    for file in tqdm(os.listdir(path)):
        ext = pathlib.Path(file).suffix[1:]
        # print(ext)
        endPath = path + "/" + file
        if os.path.isfile(endPath):
            destination = (path + "/" + "_" + ext)
            try:
                logger.write("Trying to make directory for " + ext + '\n')
                os.mkdir(destination)
            except FileExistsError:
                logger.write("Unable to make directory, does it already exist? \n")
                logger.write("moved " +  endPath +  " to " + destination + '\n')
            try:
                shutil.move(endPath, destination)
            except:
                logger.write("unable to move " + endPath + "\n")
    logger.close()

# Sorts by either year, year and month, year month and day.
def sortByDate(path, precision):
    logger = open("logs/" + str(datetime.datetime.now()).replace(':', '-').replace(".", '-') + ".txt", 'w')
    for file in tqdm(os.listdir(path)):
        endPath = path + "/" + file
        if os.path.isfile(endPath):
            modified = os.path.getmtime(endPath)
            datename = ""
            if(precision == "Y"):
                datename = datetime.datetime.fromtimestamp(modified).strftime('%Y')
            if(precision == "M"):
                datename = datetime.datetime.fromtimestamp(modified).strftime('%Y-%m')
            else:
                datename = datetime.datetime.fromtimestamp(modified).strftime('%Y-%m-%d')
            logger.write("Precision: " + datename + '\n')
            destination = (path + "/" + "_" + datename)
            try:
                logger.write("Trying to make directory for " + datename + '\n')
                os.mkdir(destination)
            except FileExistsError:
                logger.write("Unable to make directory, does it already exist?\n")
            logger.write("moved " + endPath + " to " + destination + '\n')
            try:
                shutil.move(endPath, destination)
            except:
                logger.write("unable to move " + endPath)
    logger.close()
# Uproots all files to current directory
def extract(path, FLAG):
    if FLAG == 0:
        logger = open("logs/" + str(datetime.datetime.now()).replace(':', '-').replace(".", '-') + ".txt", 'w')
        FLAG += 1
    for file in tqdm(os.listdir(path)):
        endPath = path + "/" + file
        if os.path.isdir(endPath):
            extract(endPath, FLAG)
            for temp in os.listdir(endPath):
                destination = endPath + "/" + temp
                try:
                    if FLAG == 0:
                        logger.write("Extracting " + destination + " to " + path)
                    shutil.move(destination, path)
                except:
                    if FLAG == 0:
                        logger.write("Unable to move file, does it exist already?\n")
            os.rmdir(endPath)
    if FLAG == 0:
        logger.close()
# Creates a backup before
def backup(path):
    cdate = str(datetime.datetime.now().date())
    ctime = str(datetime.datetime.now().time()).replace(":", "-")
    shutil.make_archive('dcmd_backup' + cdate + ctime, 'zip', path)
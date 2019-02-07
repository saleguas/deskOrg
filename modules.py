import os, glob
import shutil
import pathlib
import datetime
import re

# I repeat a lot of code but it's hard to get around it.
def sortByName(path, precision): #oh god this won't be fun
    for file in os.listdir(path):
        endPath = path + "/" + file
        ext = os.path.splitext(pathlib.Path(file))[0]
        if os.path.isfile(endPath):
            print(ext)

# Sort by ascending order. The precision parameter shows how make characters it should sort to.
def sortByAscending(path, precision):
    for file in os.listdir(path):
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
                            print("Couldn't move", endPath, "to", (path + '/' + dir) )
                if not moved:
                    try:
                        os.mkdir(path + "/" + ext[0:len(precision)])
                        shutil.move(endPath, path + "/" + ext[0:len(precision)])
                    except:
                        print("Couldn't move", endPath, "to", (path + '/' + dir))


# Sorts by extension of files.
def sortByExtension(path):
    for file in os.listdir(path):
        ext = pathlib.Path(file).suffix[1:]
        # print(ext)
        endPath = path + "/" + file
        if os.path.isfile(endPath):
            destination = (path + "/" + "_" + ext)
            try:
                print("Trying to make directory for", ext)
                os.mkdir(destination)
            except FileExistsError:
                print("Unable to make directory, does it already exist?")
            print("moved", endPath, "to", destination)
            try:
                shutil.move(endPath, destination)
            except:
                print("unable to move", endPath)

# Sorts by either year, year and month, year month and day.
def sortByDate(path, precision):
    for file in os.listdir(path):
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
            print(datename)
            destination = (path + "/" + "_" + datename)
            try:
                print("Trying to make directory for", )
                os.mkdir(destination)
            except FileExistsError:
                print("Unable to make directory, does it already exist?")
            print("moved", endPath, "to", destination)
            try:
                shutil.move(endPath, destination)
            except:
                print("unable to move", endPath)

# Uproots all files to current directory
def extract(path):
    for file in os.listdir(path):
        endPath = path + "/" + file
        if os.path.isdir(endPath):
            extract(endPath)
            for temp in os.listdir(endPath):
                destination = endPath + "/" + temp
                try:
                    print("Extracting", destination, "to", path)
                    shutil.move(destination, path)
                except:
                    print("Unable to move file, does it exist already?")
            os.rmdir(endPath)
# Creates a backup before
def backup(path):
    cdate = str(datetime.datetime.now().date())
    ctime = str(datetime.datetime.now().time()).replace(":", "-")
    shutil.make_archive('dcmd_backup' + cdate + ctime, 'zip', path)
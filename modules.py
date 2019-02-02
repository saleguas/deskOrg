import os, glob
import shutil
import pathlib
import datetime

def sortByExtension(path):
    for file in os.listdir(path):
        ext = pathlib.Path(file).suffix[1:]
        # print(ext)
        source = path + "/" + file
        if os.path.isfile(source):
            destination = (path + "/" + "_" + ext)
            try:
                print("Trying to make directory for", ext)
                os.mkdir(destination)
            except FileExistsError:
                print("Unable to make directory, does it already exist?")
            print("moved", source, "to", destination)
            shutil.move(source, destination)

def sortByDate(path, precision):
    for file in os.listdir(path):
        source = path + "/" + file
        if os.path.isfile(source):
            modified = os.path.getmtime(source)
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
            print("moved", source, "to", destination)
            shutil.move(source, destination)

def extract(path):
    for file in os.listdir(path):
        source = path + "/" + file
        if os.path.isdir(source):
            extract(source)
            for temp in os.listdir(source):
                destination = source + "/" + temp
                try:
                    print("Extracting", destination, "to", path)
                    shutil.move(destination, path)
                except:
                    print("Unable to move file, does it exist already?")
            os.rmdir(source)

def backup(path):
    cdate = str(datetime.datetime.now().date())
    ctime = str(datetime.datetime.now().time()).replace(":", "-")
    shutil.make_archive('dcmd_backup' + cdate + ctime, 'zip', path)
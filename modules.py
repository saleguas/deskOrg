import os, glob
import shutil
import pathlib

def sortByExtension(path):
    for file in os.listdir(path):
        ext = pathlib.Path(file).suffix[1]
        print(ext)
        if "." in file:
            destination = (path + "/" + "_" + ext )
            source = path + "/" + file
            try:
                print("Trying to make directory for", ext)
                os.mkdir(destination)
            except FileExistsError:
                print("Unable to make directory, does it already exist?")
            print("moved", source, "to", destination)
            shutil.move(source, destination)


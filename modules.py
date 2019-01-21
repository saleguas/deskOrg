import os
import shutil

def sortByName(path):
    for file in os.listdir(path):
        if "." in file:
            destination = (path + "/" + "_" + file[file.index(".") + 1:] )
            source = path + "/" + file
            try:
                os.mkdir(destination)
            except FileExistsError:
                print("it exists")
            print(destination)
            print(source)
            shutil.move(source, destination)
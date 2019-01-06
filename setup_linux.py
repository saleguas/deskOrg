from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna", "os", "gi", "shutil"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Desktop organizer",
    options = options,
    version = "1.0.3",
    description = 'Organizes files into folders',
    executables = executables
)
#thanks to Maria Irudaya for this
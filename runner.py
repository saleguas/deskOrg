from os import listdir, mkdir
from shutil import move
from sys import argv, exit

from PySide2.QtWidgets import *
from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import *


class OptionWindow(QMainWindow):
    def __init__(self, parent=None):
        super(OptionWindow, self).__init__(parent)
        self.boxarr = [0, 0, 0]
        self.layout = QVBoxLayout()
        #finishing up
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.loadBoxes()
        for box in range(len(self.boxarr2)):
            self.boxarr[box] = self.boxarr2[box].isChecked()

    def loadBoxes(self):
        #checkboxes
        self.firstBox = QCheckBox("Delete original files")
        self.secondBox = QCheckBox("Sort based on extension")
        self.thirdBox = QCheckBox("Sort based on name")
        self.boxarr2 = [self.firstBox, self.secondBox, self.thirdBox]
        #adding boxes
        self.layout.addWidget(self.firstBox)
        self.layout.addWidget(self.secondBox)
        self.layout.addWidget(self.thirdBox)

    def getStates(self):
        return[box.isChecked() for box in self.boxarr2]

#####################################################################

class MainWindow(QWidget):


    def __init__(self):
        QWidget.__init__(self)
        #misc stuff
        self.title = "Desktop organizer"
        self.layout = QVBoxLayout()
        #buttons
        self.dirbutton = QPushButton("Choose directory")
        self.gobutton = QPushButton("Start")
        self.options = QPushButton("Options")
        #Labels
        self.pathlabel = QLabel()
        #setting attributes
        self.pathlabel.setText('No directory selected')
        self.pathlabel.setAlignment(Qt.AlignCenter)
        self.dirbutton.clicked.connect(self.findDir)
        self.gobutton.clicked.connect(self.start)
        self.options.clicked.connect(self.opt)
        #Adding to layout
        self.layout.addWidget(self.dirbutton)
        self.layout.addWidget(self.options)
        self.layout.addWidget(self.pathlabel)
        self.layout.addWidget(self.gobutton)
        self.setLayout(self.layout)



    def opt(self):
        self.SW = OptionWindow()
        self.SW.resize(300, 300)
        self.SW.show()


    def findDir(self):
        filename = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        print(filename)
        self.pathlabel.setText(filename)


    def start(self):

        if self.pathlabel.text() != "No directory selected":
            for file in os.listdir(self.pathlabel.text()):
                if "." in file:
                    destination = (self.pathlabel.text() + "/" + "_" + file[file.index(".") + 1:] )
                    source = self.pathlabel.text() + "/" + file
                    try:
                        os.mkdir(destination)
                    except FileExistsError:
                        print("it exists")
                    print(destination)
                    print(source)
                    move(source, destination)





############################################################################
def go():
    app = QApplication(argv)
    widget = MainWindow()
    widget.resize(300, 300)
    widget.show()
    exit(app.exec_())

go()

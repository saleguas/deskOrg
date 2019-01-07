from os import listdir, mkdir
from shutil import move
from sys import argv, exit

from PySide2.QtWidgets import *
from PySide2.QtCore import Slot, Qt



class MainWindow(QWidget):

    filepath = ""


    def __init__(self):
        QWidget.__init__(self)



        self.dirbutton = QPushButton("Choose directory")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.dirbutton)
        self.pathlabel = QLabel()
        self.pathlabel.setText('No directory selected')
        self.pathlabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.pathlabel)
        self.gobutton = QPushButton("Start")
        self.layout.addWidget(self.gobutton)
        self.setLayout(self.layout)
        # Connecting the signal
        self.dirbutton.clicked.connect(self.findDir)
        self.gobutton.clicked.connect(self.start)


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
                    shutil.move(source, destination)

app = QApplication(argv)

widget = MainWindow()
widget.resize(300, 100)
widget.show()

exit(app.exec_())
		



############################################################################


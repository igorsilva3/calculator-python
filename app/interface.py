from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtWidgets import QApplication
import os

class Application(object):
    def __init__(self, argv):
        self.init_app = QApplication(argv)

    def get_ui_file(self, folder, filename):
        """ Returns ui file directory """

         # Gets the package path
        directory_abs = os.path.dirname(os.path.abspath(__file__))

        # Gets the path of UI folder 
        directory_ui = os.path.join(directory_abs, folder)

        # Gets the path of the UI file
        file = os.path.join(directory_ui, filename)

        return file

    def loadUiWidget(self, file):
        """ Returns the window object  """

        # Reads the UI file
        ui_file = QFile(file)

        # Prepares to load the UI 
        loader = QUiLoader()
        window = loader.load(ui_file)

        # Ends reading the UI file
        ui_file.close()

        return window

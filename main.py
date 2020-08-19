from app.program import Calculator
from PySide2.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    MainWindow = Calculator()
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

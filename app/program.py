from PySide2 import QtGui, QtCore, QtWidgets
from app.interface import Ui_MainWindow

class Calculator(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setupUi(self)

        self.btn0.clicked.connect(lambda: self.calculation(self.btn0.text()))
        self.btn1.clicked.connect(lambda: self.calculation(self.btn1.text()))
        self.btn2.clicked.connect(lambda: self.calculation(self.btn2.text()))
        self.btn3.clicked.connect(lambda: self.calculation(self.btn3.text()))
        self.btn4.clicked.connect(lambda: self.calculation(self.btn4.text()))
        self.btn5.clicked.connect(lambda: self.calculation(self.btn5.text()))
        self.btn6.clicked.connect(lambda: self.calculation(self.btn6.text()))
        self.btn7.clicked.connect(lambda: self.calculation(self.btn7.text()))
        self.btn8.clicked.connect(lambda: self.calculation(self.btn8.text()))
        self.btn9.clicked.connect(lambda: self.calculation(self.btn9.text()))
        self.btnVirg.clicked.connect(lambda: self.calculation(self.btnVirg.text()))
        self.btnMult.clicked.connect(lambda: self.calculation(self.btnMult.text()))
        self.btnSub.clicked.connect(lambda: self.calculation(self.btnSub.text()))
        self.btnAdic.clicked.connect(lambda: self.calculation(self.btnAdic.text()))
        self.btnDiv.clicked.connect(lambda: self.calculation(self.btnDiv.text()))
        self.btnClear.clicked.connect(lambda: self.clear(self.btnClear.text()))
    
    def calculation(self, arg):
        if arg == ",":
            self.display.display(".")
            
        self.display.display(arg)
    
    def clear(self, arg):
        self.display.display("0")

from PySide2 import QtGui, QtCore, QtWidgets
from app.interface import Ui_MainWindow

class Calculator(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setupUi(self)

        self.numbers = ""

        self.btn0.clicked.connect(lambda: self.set_text_display(self.btn0.text()))
        self.btn1.clicked.connect(lambda: self.set_text_display(self.btn1.text()))
        self.btn2.clicked.connect(lambda: self.set_text_display(self.btn2.text()))
        self.btn3.clicked.connect(lambda: self.set_text_display(self.btn3.text()))
        self.btn4.clicked.connect(lambda: self.set_text_display(self.btn4.text()))
        self.btn5.clicked.connect(lambda: self.set_text_display(self.btn5.text()))
        self.btn6.clicked.connect(lambda: self.set_text_display(self.btn6.text()))
        self.btn7.clicked.connect(lambda: self.set_text_display(self.btn7.text()))
        self.btn8.clicked.connect(lambda: self.set_text_display(self.btn8.text()))
        self.btn9.clicked.connect(lambda: self.set_text_display(self.btn9.text()))
        self.btnVirg.clicked.connect(lambda: self.set_text_display(self.btnVirg.text()))
        self.btnMult.clicked.connect(lambda: self.set_text_display(self.btnMult.text()))
        self.btnSub.clicked.connect(lambda: self.set_text_display(self.btnSub.text()))
        self.btnAdic.clicked.connect(lambda: self.set_text_display(self.btnAdic.text()))
        self.btnDiv.clicked.connect(lambda: self.set_text_display(self.btnDiv.text()))
        self.btnParent1.clicked.connect(lambda: self.set_text_display(self.btnParent1.text()))
        self.btnParent2.clicked.connect(lambda: self.set_text_display(self.btnParent2.text()))
        self.btnClear.clicked.connect(lambda: self.clear())
        self.btnResult.clicked.connect(lambda: self.calculation())
    
    def set_text_display(self, num):
        self.numbers = self.numbers + num 
        self.display.setText(self.numbers)
    
    def calculation(self):
        """ Returns the calculation of the equation on the display """
        try:
            # Performs the calculation
            result = str(eval(self.numbers)) 

            # Reset the numbers
            self.numbers = ""

            # Clear the display
            self.display.setText(self.numbers)

            # Puts the result on the display
            self.set_text_display(result)

        except:
            self.numbers = ""
            self.display.setText(self.numbers)
            self.set_text_display(" error ")
        
    def clear(self):
        self.numbers = ""
        self.display.setText("0")

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import calc_ui, credit_ui

class calculator(QMainWindow):

    def __init__ (self):
        QMainWindow.__init__(self)

        self.calc = calc_ui.calcWindow()
        self.credit = credit_ui.creditWindow()

        #self.calc.ui.cre.clicked.connect(self.credit)
        self.calc.ui.add.clicked.connect(self.add_button)
        self.calc.ui.sub.clicked.connect(self.sub_button)
        self.calc.ui.multiply.clicked.connect(self.multiply_button)
        self.calc.ui.Div.clicked.connect(self.div_button)

        self.calc.ui.cre.clicked.connect(self.credit_button)
        self.credit.ui.goBack.clicked.connect(self.goBack_button)

    def credit_button(self):
        self.credit.ui.credit_name.setText("Mehadi Hassan")
        self.calc.hide_window()
        self.credit.show_window()

    def goBack_button(self):
        self.credit.hide_window()
        self.calc.show_window()


    def add_button(self):
        num01 = int(self.calc.ui.num01.text())
        num02 = int(self.calc.ui.num02.text())
        output = num01 + num02
        # output = "Addition is " + str(output)
        output = (f'Addition is  {str(output)}')
        self.calc.ui.ans.setText(output)

    def sub_button(self):
        num01 = int(self.calc.ui.num01.text())
        num02 = int(self.calc.ui.num02.text())
        output = num01 - num02
        output = "Subtracton is " + str(output)
        self.calc.ui.ans.setText(output)

    def multiply_button(self):
        num01 = int(self.calc.ui.num01.text())
        num02 = int(self.calc.ui.num02.text())
        output = num01 * num02
        output = "Multiplication is " + str(output)
        self.calc.ui.ans.setText(output)

    def div_button(self):
        num01 = int(self.calc.ui.num01.text())
        num02 = int(self.calc.ui.num02.text())
        output = num01 / num02
        output = "Division is " + str(output)
        self.calc.ui.ans.setText(output)


    def show_calculator_window(self):
        self.calc.show()

    def show_credit_window(self):
        self.credit.show()

    def initialize_and_show(self):
        self.show_calculator_window()
        #self.show_credit_window()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    calculator_window = calculator()
    #calculator_window.calc.show()
    calculator_window.initialize_and_show()
    sys.exit(app.exec_())
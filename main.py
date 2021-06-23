import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import calc_ui

class calculator(QMainWindow):

    def __init__ (self):
        QMainWindow.__init__(self)
        self.calc = calc_ui.calcWindow()
        self.calc.ui.add.clicked.connect(self.add_button)
        self.calc.ui.sub.clicked.connect(self.sub_button)
        self.calc.ui.multiply.clicked.connect(self.multiply_button)
        self.calc.ui.Div.clicked.connect(self.div_button)

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

    def initialize_and_show(self):
        self.show_calculator_window()
        #self.populate_port_list()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    calculator_window = calculator()
    calculator_window.initialize_and_show()
    sys.exit(app.exec_())
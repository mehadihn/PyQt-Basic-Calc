from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
import credit

class creditWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = credit.Ui_credit()
        self.ui.setupUi(self)


    def show_window(self):
        self.show()
        pass
    def hide_window(self):
        self.hide()
        pass
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
import calc

class calcWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = calc.Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def show_window(self):
        self.show()
        pass
    def hide_window(self):
        self.hide()
        pass
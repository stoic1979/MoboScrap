import sys
import os
from PyQt5 import QtGui, QtCore, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.uic import loadUi

DIRPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)))


class MoboScrap(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi(os.path.join(DIRPATH, 'MoboScrap.ui'), self)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MoboScrap()
    window.show()
    sys.exit(app.exec_())

import sys
import os
from PyQt5 import QtGui, QtCore, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.uic import loadUi

import json

DIRPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)))

from itunes.lookup import Lookup


class MoboScrap(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi(os.path.join(DIRPATH, 'MoboScrap.ui'), self)

        # button event handlers
        self.btnItunesSearch.clicked.connect(self.handleItunesSearch)

    def handleItunesSearch(self):
        id = int(self.teId.toPlainText())
        print(id)
        lookup = Lookup()
        content = lookup.search_by_id(id)
        print("Content: %s" % content)

        # parsing json resp from itunes server
        j = json.loads(content)
        for result in j["results"]:
            print result


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MoboScrap()
    window.show()
    sys.exit(app.exec_())

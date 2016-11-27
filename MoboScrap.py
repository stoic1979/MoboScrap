import sys
import os
from PyQt5 import QtGui, QtCore, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem
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

        self.cbCountries.addItem("US")

    def handleItunesSearch(self):
        id = int(self.teId.toPlainText())
        print(id)
        lookup = Lookup()
        content = lookup.search_by_id(id)
        print("Content: %s" % content)

        # parsing json resp from itunes server
        j = json.loads(content)
        setHeader = False
        for result in j["results"]:

            # set table header once, from first record
            if not setHeader:
                self.tabItunesSearchResults.setHorizontalHeaderLabels(result.keys())
                setHeader = True
            rowPosition = self.tabItunesSearchResults.rowCount()
            self.tabItunesSearchResults.insertRow(rowPosition)
            colPosition = 0
            for k in result.keys():
                self.tabItunesSearchResults.setItem(rowPosition, colPosition, QTableWidgetItem(str(result[k])))
                colPosition += 1


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MoboScrap()
    window.show()
    sys.exit(app.exec_())

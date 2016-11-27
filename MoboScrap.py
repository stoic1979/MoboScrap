import sys
import os
import json

from PyQt5 import QtGui, QtCore, uic
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (
        QApplication, QWidget, QMainWindow,
        QMessageBox,
        QTableWidgetItem)

from itunes.lookup import Lookup
from constants.countries import countries

DIRPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)))


class MoboScrap(QMainWindow):

    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi(os.path.join(DIRPATH, 'MoboScrap.ui'), self)

        # adding button event handlers
        self.btnItunesSearch.clicked.connect(self.handleItunesSearch)

        # populating country names
        for country in countries:
            self.cbCountries.addItem(country["name"])

    def handleItunesSearch(self):

        # ensuring that id is specified in ui
        if not self.teId.toPlainText():
            msg = "Id not specified"
            print(msg)
            self._show_error_message(msg)
            return

        id = int(self.teId.toPlainText())
        print(id)
        lookup = Lookup()
        content = lookup.search_by_id(id)
        print("Content: %s" % content)

        # parsing json resp from itunes server
        j = json.loads(content)
        setHeader = False
        for result in j["results"]:

            # setting table widget's header once, from first record
            if not setHeader:
                self.tabItunesSearchResults.setHorizontalHeaderLabels(
                        result.keys())
                setHeader = True
            rowPosition = self.tabItunesSearchResults.rowCount()
            self.tabItunesSearchResults.insertRow(rowPosition)
            colPosition = 0

            # iterating all results and showing in table widget
            for k in result.keys():
                self.tabItunesSearchResults.setItem(
                        rowPosition, colPosition,
                        QTableWidgetItem(str(result[k])))
                colPosition += 1

        # checking country
        country_name = str(self.cbCountries.currentText())
        print("Country Name: %s" % country_name)

    def _show_error_message(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information) 
        msg.setText(text)
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Error !!!")
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
	
        retval = msg.exec_()
        print "Value of pressed message box button:", retval


if __name__ == '__main__':

    # instantiating & showing main window
    app = QApplication(sys.argv)
    window = MoboScrap()
    window.show()
    sys.exit(app.exec_())

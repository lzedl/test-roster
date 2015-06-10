# -*- coding: utf8 -*-
from __future__ import unicode_literals
from widgets.ui.infowindowui import Ui_InfoWindow
from PyQt4 import QtCore, QtGui


class InfoWindow(QtGui.QWidget):
    back = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_InfoWindow()
        self.ui.setupUi(self)

    def nextElement(self):
        pass

    def previousElement(self):
        pass

    def setData(self, data):
        self.ui.FIO.setText("ФИО: %s" % " ".join((data["last_name"], data["real_name"], data["second_name"])))
        if data.get("description", None):
            self.ui.Description.setText("Описание: %s" % data["description"])
        self.ui.ItemHolder.clear()
        if data.get("records", []):
            self.ui.ItemHolder.fillData(data.get("elements"))

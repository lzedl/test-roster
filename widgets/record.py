# -*- coding: utf8 -*-
from __future__ import unicode_literals
from widgets.ui.recordui import Ui_Record
from PyQt4 import QtCore, QtGui


class Element(QtGui.QWidget):
    def __init__(self, parent=None, data=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Record()
        self.ui.setupUi(self)
        if data:
            self.ui.Type.setText(data.get("type", ""))
            self.ui.Description.setText(data.get("description", ""))
            self.ui.ID.setText("ID: %s" % data.get("id", ""))

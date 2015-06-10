# -*- coding: utf8 -*-
from widgets.ui.mainwindowui import Ui_Roster
from PyQt4 import QtCore, QtGui
from other import rosterd


class Roster(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Roster()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Dialog)  # | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint)
        self.setFixedSize(200, 480)
        self.ui.Info.hide()
        self.ui.Info.ui.Back.clicked.connect(self.toggleInfo)

    def toggleInfo(self):
        if self.ui.Info.isHidden():
            self.ui.Info.show()
            self.setFixedSize(640, 480)
            self.ui.Info.ui.Filter.setFocus(QtCore.Qt.ActiveWindowFocusReason)
            # self.ui.Info.ui.Name.setFocus(QtCore.Qt.ActiveWindowFocusReason)
        else:
            self.ui.Info.hide()
            self.setFixedSize(200, 480)
            self.ui.Contacts.ui.SearchLine.setFocus(QtCore.Qt.ActiveWindowFocusReason)

    def nextElement(self):
        if self.ui.Info.isHidden():
            self.ui.Contacts.nextElement()
        else:
            self.ui.Info.nextElement()

    def previousElement(self):
        if self.ui.Info.isHidden():
            self.ui.Contacts.previousElement()
        else:
            self.ui.Info.previousElement()

    def show(self):
        self.move(0, (QtGui.qApp.desktop().screen().height() - self.height()) / 2)
        QtGui.QWidget.show(self)

    def moveEvent(self, event):
        self.move(0, (QtGui.qApp.desktop().screen().height() - self.height()) / 2)

    def enter(self):
        if self.ui.Info.isHidden():
            contactID = self.ui.Contacts.getSelectedContactID()
            if contactID:
                self.ui.Info.setData(rosterd.roster.getContactData(contactID))
                self.toggleInfo()
        else:
            self.toggleInfo()

    def escape(self):
        if self.ui.Info.isHidden():
            self.hide()
        else:
            self.toggleInfo()

    def looseFocus(self):
        if not self.ui.Info.isHidden():
            self.toggleInfo()
        self.hide()

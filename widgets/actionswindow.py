from widgets.ui.actionswindowui import Ui_ActionsWindow
from other.fuzzy import fuzzyFilter
from PyQt4 import QtCore, QtGui


class ActionsWindow(QtGui.QWidget):
    back = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_ActionsWindow()
        self.ui.setupUi(self)
        self.commands = [
            "Meta: Edit",
            "ICQ: Edit",
            "ICQ: Message",
            "Jabber: Edit",
            "Jabber: Message",
            "VK: Edit",
            "VK: Message",
        ]

    def keyPressEvent(self, event):
        key = event.key()
        # if key == QtCore.Qt.Key_Escape:
        #     self.back.emit()
        # else:
        #     QtGui.QWidget.keyPressEvent(self, event)

    def filter(self, pattern):
        self.ui.Commands.clear()
        self.ui.Commands.addItems(fuzzyFilter(unicode(pattern), self.commands))
        self.ui.Commands.setCurrentRow(0)

    def nextElement(self):
        self.ui.Commands.setCurrentRow((self.ui.Commands.currentRow() + 1) % self.ui.Commands.count())

    def previousElement(self):
        self.ui.Commands.setCurrentRow((self.ui.Commands.currentRow() - 1) % self.ui.Commands.count())

from PyQt4 import QtCore, QtGui


class KeyboardMenu(QtGui.QListWidget):
    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Enter:
            pass

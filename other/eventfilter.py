from PyQt4 import QtCore, QtGui


class GlobalEventFilter(QtCore.QObject):
    roster = None

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Down:
                self.roster.nextElement()
                return True
            elif event.key() == QtCore.Qt.Key_Up:
                self.roster.previousElement()
                # self.roster.ui.ContactList.event(event)
                return True
            elif event.key() == QtCore.Qt.Key_Return:
                self.roster.enter()
                return True
            elif event.key() == QtCore.Qt.Key_Tab:
                return True
            elif event.key() == QtCore.Qt.Key_Escape:
                self.roster.escape()
                return True
            else:
                if self.roster.ui.Info.isHidden():
                    self.roster.ui.Contacts.ui.SearchLine.event(event)
                else:
                    self.roster.ui.Info.ui.Filter.event(event)
                return True
        elif event.type() == QtCore.QEvent.ApplicationDeactivate:
            self.roster.looseFocus()
            return True
        if event.type() == QtCore.QEvent.MouseButtonPress and unicode(obj.objectName()) in (u"SearchLine", u"Command"):
            return True
        return False


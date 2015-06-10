from other.contactproxymodel import ContactsProxyModel
from widgets.ui.contactsui import Ui_Contacts
from PyQt4 import QtCore, QtGui
from other import rosterd


class Contacts(QtGui.QWidget):
    showContact = QtCore.pyqtSignal(unicode)

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Contacts()
        self.ui.setupUi(self)
        self.ui.SearchLine.setFocus(QtCore.Qt.ActiveWindowFocusReason)
        self.contactsModel = QtGui.QStandardItemModel(self)
        self.proxyModel = ContactsProxyModel(self)
        self.proxyModel.setDynamicSortFilter(True)

        self.proxyModel.setSourceModel(self.contactsModel)
        # self.ui.ContactList.setModel(self.proxyModel)

        self.contacts = rosterd.roster.getFullList()
        self.contacts.sort(key=lambda x: x[1])
        self.contactListItems = []

        for n, (contactID, name) in enumerate(self.contacts):
            item = QtGui.QStandardItem(name)
            item.score = n
            item.contactID = contactID
            self.contactListItems.append(item)
            self.contactsModel.appendRow(item)
        self.completer = QtGui.QCompleter(self.proxyModel, self.ui.SearchLine)
        self.ui.SearchLine.setCompleter(self.completer)

    def filter(self, pattern):
        self.proxyModel.pattern = pattern
        self.proxyModel.invalidateFilter()
        self.proxyModel.sort(0)
        # self.ui.ContactList.clear()
        # self.ui.ContactList.addItems(fuzzyFilter(unicode(pattern), self.contacts))
        # self.ui.ContactList.setCurrentRow(0)

    def nextElement(self):
        index = self.ui.ContactList.currentIndex()
        if index.isValid():
            self.ui.ContactList.setCurrentIndex(
                self.proxyModel.index((index.row() + 1) % self.proxyModel.rowCount(), 0)
            )
        else:
            self.ui.ContactList.setCurrentIndex(self.proxyModel.index(0, 0))
        # self.ui.ContactList.setCurrentRow((self.ui.ContactList.currentRow() + 1) % self.ui.ContactList.count())

    def previousElement(self):
        index = self.ui.ContactList.currentIndex()
        if index.isValid():
            self.ui.ContactList.setCurrentIndex(
                self.proxyModel.index((index.row() - 1) % self.proxyModel.rowCount(), 0)
            )
        else:
            self.ui.ContactList.setCurrentIndex(self.proxyModel.index(self.proxyModel.rowCount() - 1, 0))
        # self.ui.ContactList.setCurrentRow((self.ui.ContactList.currentRow() - 1) % self.ui.ContactList.count())

    def getSelectedContactID(self):
        # if self.ui.ContactList.currentRow() != -1:
        #     for item in self.contacts:
        #         if item[1] == unicode(self.ui.ContactList.currentItem().text()):
        #             return item[0]
        index = self.ui.ContactList.currentIndex()
        if index.isValid():
            return self.contactsModel.itemFromIndex(index).contactID
        return None

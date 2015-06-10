# -*- coding: utf8 -*-
from PyQt4 import QtCore, QtGui
from record import Element


class ItemHolder(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(self.sizeHint())
        self.elements = []

        self.setLayout(QtGui.QVBoxLayout())
        self.layout().addStretch()
        self.layout().setMargin(4)
        self.layout().setSpacing(3)

    def filter(self, pattern):
        pass

    def fillData(self, elements):
        for element in elements:
            item = Element(self, element)
            self.elements.append(item)
            self.layout().insertWidget(len(self.elements)-1, item)
        self.resize(self.sizeHint())

    def clear(self):
        for element in self.elements:
            element.close()
        self.elements = []

# -*- coding: utf8 -*-
from PyQt4 import QtGui


class ContactsProxyModel(QtGui.QSortFilterProxyModel):
    pattern = ""

    def __init__(self, parent=None):
        QtGui.QSortFilterProxyModel.__init__(self, parent)

    def lessThan(self, left, right):
        return self.sourceModel().itemFromIndex(left).score < self.sourceModel().itemFromIndex(right).score

    def filterAcceptsRow(self, row, index):
        item = self.sourceModel().item(row)
        lower = item.text().toLower()
        score = 0
        cn = -1
        wl = lower.length()
        for n, c in enumerate(self.pattern, 1):
            for cn in xrange(cn + 1, wl):
                c2 = lower[cn]
                if c == c2:
                    break
                else:
                    score += n
            else:
                return False
        else:
            item.score = score
            return True

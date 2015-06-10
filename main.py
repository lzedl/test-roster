from other.eventfilter import GlobalEventFilter
from widgets.mainwindow import Roster
from other.xhook2 import HookManager
from PyQt4 import QtGui
import sys


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    eventFilter = GlobalEventFilter()
    hookManager = HookManager()
    mainWindow = Roster()
    hookManager.hotKey.connect(mainWindow.show)
    eventFilter.roster = mainWindow
    app.installEventFilter(eventFilter)

    mainWindow.move(0, (app.desktop().screen().height() - mainWindow.height()) / 2)
    mainWindow.show()
    hookManager.start()

    ret = app.exec_()
    hookManager.terminate()
    sys.exit(ret)
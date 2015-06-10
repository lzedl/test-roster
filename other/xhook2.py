# -*- coding: utf8 -*-
from PyQt4 import QtCore
import Xlib.display
import Xlib.X


class HookManager(QtCore.QThread):
    hotKey = QtCore.pyqtSignal()

    def __init__(self):
        QtCore.QThread.__init__(self)
        display = Xlib.display.Display()
        self.root = display.screen().root
        self.root.change_attributes(event_mask=Xlib.X.KeyPressMask)
        # set keyboard shortcut to "c"
        self.root.grab_key(54, Xlib.X.Mod4Mask, 0, Xlib.X.GrabModeAsync, Xlib.X.GrabModeAsync)
        # self.root.grab_pointer(
        #     True, Xlib.X.PointerMotionMask, Xlib.X.GrabModeAsync,
        #     Xlib.X.GrabModeAsync, Xlib.X.NONE, Xlib.X.NONE, Xlib.X.CurrentTime
        # )
        # display.allow_events(Xlib.X.GrabModeAsync, Xlib.X.CurrentTime)

    def run(self):
        while True:
            event = self.root.display.next_event()  # should block until key pressed
            if event.type == Xlib.X.MotionNotify:
                print event.root_x, event.root_y
            else:
                self.hotKey.emit()

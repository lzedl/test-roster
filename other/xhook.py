# -*- coding: utf8 -*-
from Xlib import X, XK, display
from Xlib.ext import record
from Xlib.protocol import rq
from PyQt4 import QtCore
# import threading
import time
import sys


class HookManager(QtCore.QThread):
    hotKey = QtCore.pyqtSignal()

    def __init__(self):
        # threading.Thread.__init__(self)
        QtCore.QThread.__init__(self)
        # self.finished = threading.Event()

        # Hook to our display.
        self.localDisplay = display.Display()
        self.recordDisplay = display.Display()

        # prepare keysim dict
        self.keysDict = {}
        for name in dir(XK):
            if name.startswith("XK_"):
                self.keysDict[getattr(XK, name)] = name.lstrip("XK_")

        self.isModifier = False

    def run(self):
        # Check if the extension is present
        if not self.recordDisplay.has_extension("RECORD"):
            print "RECORD extension not found"
            sys.exit(1)
        # r = self.recordDisplay.record_get_version(0, 0)
        # print "RECORD extension version %d.%d" % (r.major_version, r.minor_version)

        # Create a recording context; we only want key events
        self.context = self.recordDisplay.record_create_context(
            0,
            [record.AllClients],
            [
                {
                    "core_requests": (0, 0),
                    "core_replies": (0, 0),
                    "ext_requests": (0, 0, 0, 0),
                    "ext_replies": (0, 0, 0, 0),
                    "delivered_events": (0, 0),
                    "device_events": (X.KeyPress, X.KeyRelease),
                    "errors": (0, 0),
                    "client_started": False,
                    "client_died": False
                }
            ]
        )

        # Enable the context; this only returns after a call to record_disable_context,
        # while calling the callback function in the meantime
        self.recordDisplay.record_enable_context(self.context, self.processEvents)
        # Finally free the context
        self.recordDisplay.record_free_context(self.context)

    def cancel(self):
        # self.finished.set()
        self.terminate()
        self.localDisplay.record_disable_context(self.context)
        self.localDisplay.flush()

    def processEvents(self, reply):
        if reply.category != record.FromServer:
            return
        if reply.client_swapped:
            print "* received swapped protocol data, cowardly ignored"
            return
        if not len(reply.data) or ord(reply.data[0]) < 2:
            # not an event
            return
        data = reply.data
        while len(data):
            event, data = rq.EventField(None).parse_binary_value(data, self.recordDisplay.display, None, None)
            if event.type == X.KeyPress:
                # keysym = self.localDisplay.keycode_to_keysym(event.detail, 0)
                # print "Key press", self.keysDict.get(keysym, keysym)
                if event.detail == 133:  # If key code == Super_L
                    self.isModifier = True
                if event.detail == 54 and self.isModifier:
                    self.hotKey.emit()
            elif event.type == X.KeyRelease:
                # keysym = self.localDisplay.keycode_to_keysym(event.detail, 0)
                # print "Key release", self.keysDict.get(keysym, keysym)
                if event.detail == 133:  # If key code == Super_L
                    self.isModifier = False


if __name__ == "__main__":
    hm = HookManager()
    hm.start()
    time.sleep(10)
    hm.cancel()
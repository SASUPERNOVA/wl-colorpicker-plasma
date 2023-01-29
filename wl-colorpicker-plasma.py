#!/usr/bin/python3

from PyQt6.QtDBus import QDBusConnection, QDBusMessage, QDBusPendingReply, QDBusPendingCallWatcher
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QColor
import sys

def colorPicked():
    reply = QDBusPendingReply(call)
    if reply.isError():
        print(reply.error().message())
    else:
        print(QColor(reply.argumentAt(0)[0]).name())
        
app = QCoreApplication(sys.argv)
msg = QDBusMessage.createMethodCall("org.kde.KWin", "/ColorPicker", "org.kde.kwin.ColorPicker", "pick")
call = QDBusConnection.sessionBus().asyncCall(msg)
watcher = QDBusPendingCallWatcher(call, app)
watcher.finished.connect(colorPicked)
watcher.waitForFinished()

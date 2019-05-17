import threading
import sys


class MainHandler (threading.Thread):

    def __init__(self,clientHelper):
        threading.Thread.__init__(self)
        self._clientHelper =clientHelper

    def start(self):
        while True:
            msg = sys.stdin.readline()
            self._clientHelper.sendMsg(msg)



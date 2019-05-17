import threading


class SendThread (threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self._client = client

    def run(self):
        while True:
            self._client.doSend()


class RecvThread(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self._client = client

    def run(self):
        while True:
            self._client.recv(1024)


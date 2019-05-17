import socket
import queue
import threading
from zm.ircbot.util.IOUtil import IoUtil
from zm.ircbot.ircthread.MsgSendThread import RecvThread
from zm.ircbot.ircthread.MsgSendThread import SendThread
sendLock = threading.Lock()
recvLock = threading.Lock()
class Client:
    def __init__(self,host,port):
        self._host = host
        self._port = port
        self._clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._inQueue = queue.Queue()
        self._outQueue = queue.Queue()


    def sendMessage(self,msg):
        self._outQueue.put(msg)


    def sendMessageImmde(self,msg):
        with sendLock:
            self._clientSocket.send(msg.encode())


    def doSend(self):
        if not self._outQueue.empty():
            self.sendMessageImmde(self._outQueue.get())

    def getRecvMessage(self):
        return self._inQueue.get()

    def recv(self,length):
        with recvLock:
            data = self._clientSocket.recv(length).decode()
            if data.find('PING') != -1:
                self.sendMessageImmde('PONG ' + data.split()[1] + '\r\n')
            self._inQueue.put(data)


    def login(self,nickname,username,realname,chanel):
        self.setNickName(nickname)
        self.setChanel(chanel)
        IoUtil.print("Start to connect server . IRC host: %s, port %s" %(self.getHost(),self.getPort() ))
        cs = self._clientSocket
        cs.connect((self.getHost(), self.getPort()))
        IoUtil.print("Connected!")

        self.recv(1024)

        self.sendMessageImmde("NICK %s \r\n" % nickname)
        self.recv(1024)

        self.sendMessageImmde("USER %s %s %s :%s \r\n" %(username,username,username,realname))
        self.recv(1024)

        self.sendMessageImmde("JOIN #%s\r\n" %chanel)
        self.recv(1024)
        self._startSubThread()

    def _startSubThread(self):
        recvThread = RecvThread(self)
        recvThread.start()

        sendThread = SendThread(self)
        sendThread.start()

    def getHost(self):
        return self._host

    def getPort(self):
        return self._port

    def setChanel(self, chanel):
        self._chanel = chanel

    def setNickName(self, nickName):
        self._nickName = nickName

    def getChanel(self,):
        return self._chanel

    def tetNickName(self,):
        return self._nickName
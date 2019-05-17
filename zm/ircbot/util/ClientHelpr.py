from zm.ircbot.util.ircnet import Client
from zm.ircbot.util.IOUtil import IoUtil
from zm.ircbot.ircthread.HandleThread import MainHandler
class ClientHelper:

    def __init__(self,host,port):
        self._client = Client(host,port)

    def start(self, nickname, username, realname, chanel):
        IoUtil.print("Start login")
        self._login(nickname, username, realname, chanel)
        IoUtil.print("Login finished")
        IoUtil.print("Robot starting now!")

        mainHandler = MainHandler(self)
        #mainHandler.start()
        self.handleMessage()

    def _login(self, nickname, username, realname, chanel):
        self._client.login(nickname, username, realname, chanel)

    def handleMessage(self):
        while True:
            msg = self._client.getRecvMessage()
            IoUtil.print(msg)

    def sendMsg(self,msg):
        self._client.sendMessage(self._buildPublicMessage(msg))

    def _buildPublicMessage(self,msg):
        return "PRIVMSG #%s :%s\r\n" %(self._client.getChanel(), msg)

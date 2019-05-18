from zm.ircbot.util.ircnet import Client
from zm.ircbot.util.IOUtil import IoUtil
from zm.ircbot.handler.Handler import MainHandler
class ClientHelper:

    def __init__(self,host,port):
        self._client = Client(host,port)

    def start(self, nickname, username, realname, chanel):
        IoUtil.print("Start login")
        self._login(nickname, username, realname, chanel)
        IoUtil.print("Login finished")
        IoUtil.print("Robot starting now!")
        self.handleMessage()

    def _login(self, nickname, username, realname, chanel):
        self._client.login(nickname, username, realname, chanel)

    def handleMessage(self):
        mainHandler = MainHandler(self)
        while True:
            msg = self._client.getRecvMessage()
            if self.isChatMessate(msg):
                mainHandler.excute(msg)
            else:
                IoUtil.print(msg)
    def sendMsg(self,msg):
        self._client.sendMessage(self._buildPublicMessage(msg))

    def _buildPublicMessage(self,msg):
        return "PRIVMSG #%s :%s\r\n" %(self._client.getChanel(), msg)

    def isChatMessate(self, msg):
        return msg.find('PRIVMSG') != -1

    def isSendToMe(self,msg):
        return msg.startswith(self._client.getNickName())

    def getNickName(self):
        return self._client.getNickName()
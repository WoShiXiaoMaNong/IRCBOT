from zm.ircbot.util.IOUtil import IoUtil
import sys


class MainHandler :

    def __init__(self,clientHelper):
        self._clientHelper =clientHelper

    def excute(self,msg):
        nickFrom = msg.split('!')[0].replace(':', '')
        message = ':'.join(msg.split(':')[2:])
        if self._clientHelper.isSendToMe(message):
            IoUtil.print("%s:>>>>%s<<<<<\r\n" % (nickFrom, message.replace("\r\n", "")))
            self.sendMsg(nickFrom + ":我还在开发中~~~")
        else:
            IoUtil.print("%s %s" % (nickFrom, message))

from zm.ircbot.util.IOUtil import IoUtil
from zm.ircbot.item.IrcMsg import IrcMsg
from config.read_config import ConfigReader
from zm.ircbot.handler.HandlerBase import Handler
import concurrent.futures

class MainHandler:

    def __init__(self, client_helper):
        self._clientHelper = client_helper

        pool_size = ConfigReader.get_thread_pool_size()
        IoUtil.print("Init Thread Pool size (Handler) . size is %s\r\n" % pool_size)
        self.__ThreadPoolExecutor = concurrent.futures.ThreadPoolExecutor(pool_size)

    def execute(self, msg):
        irc_msg = IrcMsg(msg, self._clientHelper.getNickName())
        if irc_msg.is_to_me():
            IoUtil.print("%s:>>>>%s<<<<<\r\n" % (irc_msg.get_from_nick_name(), irc_msg.get_messge()))
            self.do_execute(irc_msg)
        else:
            IoUtil.print("%s %s\r\n" % (irc_msg.get_from_nick_name(),  irc_msg.get_messge()))

    def do_execute(self, msg):
        obj = None
        if msg.is_command_msg():
            handler_name = msg.get_method()
            obj = self.get_handler_ojb(handler_name)
        if obj is None:
            obj = Handler()
        self.__ThreadPoolExecutor.submit(obj.do_execute, msg, self._clientHelper)


    def get_handler_ojb(self, handler_name):
        moudle_name = ConfigReader.getMoudleName(handler_name)
        class_name = ConfigReader.getClassName(handler_name)

        if moudle_name is not None and class_name is not None:
            m = __import__(moudle_name, fromlist=True)
            class_name = getattr(m, class_name)
            obj = class_name()
            return obj
        else:
            return None


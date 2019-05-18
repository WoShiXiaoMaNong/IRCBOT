
class Handler:

    def do_execute(self, irc_msg, client_helper):
        rst = self.execute(irc_msg)
        client_helper.sendMsg(irc_msg.get_from_nick_name() + ":" + rst)

    def execute(self, irc_msg):
        return "听不懂你在说什么。。。"

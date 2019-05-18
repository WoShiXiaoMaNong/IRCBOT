import re
class IrcMsg:

    def __init__(self,irc_msg_str,self_nick_name):
        self.__irc_msg_str = irc_msg_str
        self.__self_nick_name = self_nick_name
        self.__init_fields(irc_msg_str)

    def __init_fields(self,irc_msg_str):
        self.__nick_from = irc_msg_str.split('!~')[0].replace(':', '')
        self.__host_from = irc_msg_str.split('!~')[1].split("PRIVMSG")[0]
        self.__message = ":".join(irc_msg_str.split('PRIVMSG')[1].split(":")[1:])
        if self.__message.endswith("\r\n"):
            self.__message = self.__message[:-2]

        self.__command = Command(self.get_messge())

    def is_to_me(self):
        return self.__message.find(self.__self_nick_name + ':') != -1

    def get_messge(self):
        if self.is_to_me():
            return ':'.join(self.__message.split(':')[1:])
        else:
            return self.__message

    def get_from_nick_name(self):
        return self.__nick_from

    def get_from_host(self):
        if self.__host_from.find("@"):
            return self.__host_from.strip().split('@')[1]
        return self.__host_from.strip()

    def get_method(self):
        return self.__command.get_method()

    def get_param(self):
        return self.__command.get_param()

    def is_command_msg(self):
        return self.get_method() is not None and self.get_param() is not None


class Command:

    def __init__(self,command_msg):
        self._command_msg = command_msg

    def get_method(self):
        if self.is_command_msg():
            return self._command_msg.split(':')[0]

    def get_param(self):
        if self.is_command_msg():
            return self._command_msg.split(':')[1]

    def is_command_msg(self):
        if self._command_msg.find(":") == -1:
            return False
        elif len(self._command_msg.split(':')) != 2:
            return False
        return True


if __name__ == "__main__":

    i = ":MrkkkBot   :tianqi:杭州"

import http.client
import xml.sax
import xml.sax.handler
from zm.ircbot.util.IOUtil import IoUtil
from zm.ircbot.handler.HandlerBase import Handler


class TranslateHandler(Handler):

    def __init__(self):
        Handler.__init__(self)
        self.__host = "ws.webxml.com.cn"
        self.__request = "/WebServices/TranslatorWebService.asmx/getEnCnTwoWayTranslator?Word="

    def execute(self, irc_msg):
        rst = "我不知道你在说什么"
        target_word = irc_msg.get_param()
        request = self.__request + target_word
        IoUtil.print("Start to send request %s%s\r\n" % (self.__host, request))
        conn = http.client.HTTPConnection(self.__host)
        conn.request("GET", request)
        response = conn.getresponse()
        status = response.status
        reason = response.reason
        IoUtil.print("Request result. Status %s,reason:%s\r\n" % (status, reason))
        if status == 200:
            data_xml =  response.read().decode('utf-8')
            xh = TranslateXmlHandler()
            xml.sax.parseString(data_xml,xh)
            rst = xh.get_string().replace("\r\n",":")+ "\r\n"
            print(rst)
        return rst


class TranslateXmlHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.__string = ""
        self.__currentData = ""

    def startElement(self, tag, attributes):
        self.__currentData = tag

    def characters(self, content):
        if self.__currentData == "string":
            if content != '\n' and content != '\r':
                self.__string += content

    def get_string(self):
        return self.__string

if __name__ == "__main__":
    a = TranslateHandler()
    print (a.execute('hello'))
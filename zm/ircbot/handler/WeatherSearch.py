import http.client
from zm.ircbot.util.IOUtil import IoUtil
import json
from config.read_config import ConfigReader
from zm.ircbot.handler.HandlerBase import Handler


class WeatherSearch(Handler):

    def __init__(self):
        Handler.__init__(self)
        self.__host = "www.weather.com.cn"
        self.__requset = "/data/sk/cityName.html"

    def execute(self, irc_msg):
        rst = "我不知道你在说什么"
        city_name = irc_msg.get_param()
        city_id = ConfigReader.getCityId(city_name)
        if city_id is None:
            return "我不认识" + city_name + ",无法查询。"
        request = self.__requset.replace("cityName", city_id)
        IoUtil.print("Start to send request %s%s\r\n" % (self.__host, request))
        conn = http.client.HTTPConnection(self.__host)

        conn.request("GET", request)
        response = conn.getresponse()
        status = response.status
        reason = response.reason
        IoUtil.print("Request result. Status %s,reason:%s\r\n" % (status,reason))
        if status == 200:
            weather = Weatcher(response.read().decode())
            rst = weather.getString()
        else:
            rst = "机器人遇到了未知的问题！！！奔溃中"

        return rst


class Weatcher:

    def __init__(self,json_msg):
        self.__json = json.loads(json_msg)['weatherinfo']

    def getTemp(self):
        return self._getValue('temp')

    def getCity(self):
        return self._getValue("city")

    def getAtmosphericPressure(self):
        return self._getValue("AP")

    def getHumidity(self):
        return self._getValue("SD")

    def getWindDrict(self):
        return self._getValue("WD")

    def getWindPower(self):
        return self._getValue("WS")

    def getString(self):
        return "城市：%s .温度：%s .风向：%s .风力：%s .气压：%s .湿度：%s " %(self.getCity(),self.getTemp(),self.getWindDrict(),self.getWindPower(),self.getAtmosphericPressure(),self.getHumidity())

    def _getValue(self, key):
        return self.__json[key]

if __name__ == "__main__":
    ws = WeatherSerch()
    data = ws.execute("101030300")
    print (data)
    t = Weatcher(data)

    print (t.getString())
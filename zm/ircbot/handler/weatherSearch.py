import http.client
from zm.ircbot.util.IOUtil import IoUtil
import json
from config.read_config import ConfigReader

class WeatherSerch:

    def __init__(self):
        self._host = "www.weather.com.cn"
        self._requset = "/data/sk/cityName.html"


    def search(self,cityName):

        rst = "我也不知道你在说什么"
        cityId = ConfigReader.getCityId(cityName)
        reqeust = self._requset.replace("cityName", cityId)
        IoUtil.print("Start to send request %s%s\r\n" % (self._host, reqeust))
        conn = http.client.HTTPConnection(self._host)

        conn.request("GET",reqeust)
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

    def __init__(self,jsonMsg):
        self._json = json.loads(jsonMsg)['weatherinfo']

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
    def _getValue(self,key):
        return self._json[key]
if __name__ == "__main__":
    ws = WeatherSerch()
    data = ws.search("101030300")
    print (data)
    t = Weatcher(data)

    print (t.getString())
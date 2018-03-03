from datetime import date, datetime # days_to
from urllib.request import urlopen
import json

import cred
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class owether:
    
    def __init__(self, api, ):
        self.api = api
        

    def __getjson(self, city, mode="fc"):
        self.city = city
        lang = "de"
        url_addon = city + "&units=metric" + "&lang=" + lang + "&APPID=" + self.api
        if mode == "now":
            self.url = "https://api.openweathermap.org/data/2.5/weather?q="+ url_addon
        elif mode == "fc":
            self.url = "https://api.openweathermap.org/data/2.5/forecast?q="+ url_addon
        response = urlopen(self.url).read().decode('utf-8')
        obj = json.loads(response)
        logger.debug(obj)
        return obj

    def now(self, city):
        obj = self.__getjson(city, mode= "now")
        result = {'temp_max' : obj['main']['temp_max'],
            'temp_min' : obj['main']['temp_min'],
            'sunrise' : datetime.fromtimestamp(int(obj['sys']['sunrise'])).strftime('%H:%M:%S'),
            'sunset' : datetime.fromtimestamp(int(obj['sys']['sunset'])).strftime('%H:%M:%S'),
            'condition' : obj['weather'][0]['description']}
        logger.info(result)
        return result

    def forecast(self, city):
        resultList= []
        obj = self.__getjson(city)
        logger.debug(obj)
        for item in obj['list']:
            d = {
            'time' : datetime.fromtimestamp(int(item['dt'])).strftime('%H:%M:%S'),
            'date' : datetime.fromtimestamp(int(item['dt'])).strftime('%Y-%m-%d'),
            'unixtime' : item['dt'],
            'temp' : item['main']['temp'],
            'condition' : item['weather'][0]['description'],
            'icon' : item['weather'][0]['icon'],
            }
            resultList.append(d)
            break
        #print(obj)
        print(resultList)
    

if __name__ == "__main__":
    ow = owether(cred.ow_api)
    ow.forecast("genthin")
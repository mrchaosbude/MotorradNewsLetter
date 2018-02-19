from datetime import date, datetime # days_to
from urllib.request import urlopen
import json
from newsapi import NewsApiClient
import logging
from gnewsfeed import Gnewsfeed

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
ow_api='17e753103a9079bbf84d9bb44390c8ac'
news_api= '0cbc1a2e47ad4e1e93d32abb6b329e5b'


def days_to(first_month, last_month):
    """Check if is on or off Sesson and give the days back

    Arguments:
        first_month {Int} -- the first month to ride(Numbde)
        last_month {Int} -- the last month to ride(Number)

    Returns:
        [list 0 = Boolean, 1 = days left or to] -- gives back if off or on sesson and the days
    """

    today = date.today()
    sesson = False
    day = 0
    first_month = date(today.year, first_month, 1)
    last_month = date(today.year, last_month + 1, 1)
    logger.debug("Sesson Start: %s Sesson End: %s", first_month, last_month)

    if  today > first_month: # test if sessonis on and rest days
        day = abs(last_month - today).days
        sesson = True
        logger.info('its sesson and you have %s left', day)

    if today > last_month or today < first_month: # test if sesson is off and rest days
        day = (first_month - today).days
        sesson = False
        logger.info('sesson is off and %s days before ride', day)

    return sesson, day

def open_wether(city, api, ):
    """gives back the wether condition

    Arguments:
        city {string} -- [description]
        api {string} -- [description]

    Returns:
        [dict] -- gives back the data
    """
    lang = "de"
    url_addon = city + "&units=metric" + "&lang=" + lang + "&APPID=" + api
    url = "https://api.openweathermap.org/data/2.5/weather?q="+ url_addon
    response = urlopen(url).read().decode('utf-8')
    obj = json.loads(response)
    logger.info(obj)
    result = {'temp_max' : obj['main']['temp_max'],
                'temp_min' : obj['main']['temp_min'],
                'sunrise' : datetime.fromtimestamp(int(obj['sys']['sunrise'])).strftime('%H:%M:%S'),
                'sunset' : datetime.fromtimestamp(int(obj['sys']['sunset'])).strftime('%H:%M:%S'),
                'condition' : obj['weather'][0]['description']}
    logger.info(result)
    return result

def news():
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=de&'
        'apiKey=' + news_api)
    response = urlopen(url).read().decode('utf-8')
    print (response)
    


if __name__ == "__main__":
    #print(days_to(3, 10))
    #open_wether("berlin", ow_api)
    news()

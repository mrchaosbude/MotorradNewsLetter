import feedparser
import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Gnewsfeed:
    
    def __init__(self, topic, language="DE", country=None):
        """get the data from the google news rss and hold it for use 
        
        Arguments:
            topic {string} -- [the Topic you want ]
        
        Keyword Arguments:
            language {string} -- [the language of the news] (default: {"DE"})
            country {string} -- [from where are the news if not set the same as the language(dont kow if it worke)] (default: {None})
        """

        if country == None:
            country = language

        self.feedUrl = 'https://news.google.de/news/feeds?pz=1&cf=all&ned={country}&hl={language}&q={topic}'.format(
            topic=topic, language=language, country=country)
        self.feed = feedparser.parse(self.feedUrl)
        logger.info('bozo status: {}'.format(self.feed.bozo))
        if self.feed.bozo != 0:
            raise Exception('No Conection or feed Corupt!' + self.feed.bozo_exception)  # [Bug] exception is a typeerror
        logger.info('Feed status code : {}'.format(self.feed.status))            
        logger.debug(self.feed)

    def datetimeconv(self, dtinput):
        """Converst date to datetime objekt and
            GMT/UTC to the aktuale timezone 
        
        Arguments:
            dtinput {[RFC822 date-times]} -- [its the standart rss date time format]
        
        Returns:
            [datetime objekt] -- [description]
        """

        dtoutput = datetime.datetime.strptime(dtinput, '%a, %d %b %Y %H:%M:%S %Z') # parse datum zu datetime objekt
        dtoutput = dtoutput.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None) # convertiere von gmt/utc zu hier
        return dtoutput

    def get_feedinfo(self):
        """
        Gives back the feed information as a liat

        Returns:
            [list] -- [title, link, update (datetime objekt to actuell timezone), ]
        """

        f = self.feed['feed']
        return [f['title'], f['link'], self.datetimeconv(f['updated'])]

    def get_news(self):
        """
        Giives all news from the news rss feed back as a list
        
        Returns:
            [list] -- [Titel, link, publichdate (as datetime objekt to the actuell timezone)]
        """

        r = []
        f = self.feed['entries']
        for post in f:
            l = [post.title, post.link, self.datetimeconv(post.published)]
            r.append(l)
        return r

if __name__ == "__main__":
    g = Gnewsfeed('motorrad', language="de")
    #print(g.get_feedinfo())
    #print(g.get_news())
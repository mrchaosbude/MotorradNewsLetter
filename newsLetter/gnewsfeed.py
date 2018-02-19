import feedparser
import datetime


class Gnewsfeed:
    def __init__(self, topic,):
        self.topic = topic
        self.feedUrl = 'https://news.google.com/news/rss/search/section/q/' + self.topic + '?hl=de&gl=DE&ned=de'
        self.feed = feedparser.parse(self.feedUrl)
        
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
        """Gives back the feed information as a dict
            --------schuld change to list...----------

        Returns:
            [dict] -- [title, link, date, ]
        """

        f = self.feed['feed']
        return {
                'title' : f['title'],
                'link' : f['link'],
                'date' : self.datetimeconv(f['updated'])
        }

    def get_news(self):
        r = []
        f = self.feed['entries']
        for post in f:
            l = [post.title, post.link, self.datetimeconv(post.published)]
            r.append(l)
        return r

if __name__ == "__main__":
    g = Gnewsfeed('motorrad')
    #print(g.get_feedinfo())
    g.get_news()
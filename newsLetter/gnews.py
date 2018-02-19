import requests
from bs4 import BeautifulSoup


my_headers={"Host": "www.google.com",
"User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "en-US,am;q=0.7,zh-HK;q=0.3",
"Accept-Encoding": "gzip, deflate",
"Cookie": "PREF=ID=1111111111111111:FF=0:LD=en:TM=1439993585:LM=1444815129:V=1:S=Zjbb3gK_m_n69Hqv; NID=72=F6UyD0Fr18smDLJe1NzTReJn_5pwZz-PtXM4orYW43oRk2D3vjb0Sy6Bs_Do4J_EjeOulugs_x2P1BZneufegpNxzv7rkY9BPHcfdx9vGOHtJqv2r46UuFI2f5nIZ1Cu4RcT9yS5fZ1SUhel5fHTLbyZWhX-yiPXvZCiQoW4FjZd-3Bwxq8yrpdgmPmf4ufvFNlmTd3y; OGP=-5061451:; OGPC=5061713-3:",
"Connection": "keep-alive"}


googtrends = requests.get("https://news.google.com/news/search/section/q/motorra/motorra?hl=de&gl=DE&ned=de")
my_content = googtrends.text.encode('utf-8')
soup = BeautifulSoup(my_content,'lxml')
links = soup.find_all()

#Lets try if we are getting correct content from the site
# That site contains "Apple Inc.‬, ‪App Store‬‬" so let's check it in the got response

print (links)

# It prints false so website is being rendered by JS even header change does not affect
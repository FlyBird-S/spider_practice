#coding utf8
import re
import urllib2
import urlparse

from bs4 import BeautifulSoup

response = urllib2.urlopen(r"https://baike.baidu.com/item/%E9%AD%94%E6%B3%95/194834")
if response.getcode() != 200:
    print response.getcode()
list = response.read()
soup = BeautifulSoup(list,'html.parser',from_encoding='utf-8')
links = soup.find_all('a',href = re.compile(r"/item/.*"))
for link in  links:
    print urlparse.urljoin(r"https://baike.baidu.com/item/%E9%AD%94%E6%B3%95/194834",link['href'])

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
# print "get all url"
# link = soup.find_all('a')
# for l in link:
#     print l.name,l['href'],l.get_text()
# print r"get 'lacie' url"
# link_2 = soup.find('a',href='http://example.com/lacie')
# print link_2.name,link_2['href'],link_2.get_text()
# print r"get regular expression url"
# link_2 = soup.find('a',href=re.compile(r"ill"))
# print link_2.name,link_2['href'],link_2.get_text()
#
# print r"get P  paragraph  text"
# link_2 = soup.find('p',class_='story')
# print link_2.name,link_2.get_text()


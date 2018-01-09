# coding=utf-8
import re
import urlparse
from bs4 import BeautifulSoup
import urllib2
class HtmlParser(object):
    def parse(self, url, html_cont):
        if url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(url,soup)
        new_data = self._get_new_data(url,soup)
        return new_urls,new_data

    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a',href = re.compile(r"/item/(.*)"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(url,new_url) #使url完整
            new_urls.add(new_full_url)
        return new_urls
    def _get_new_data(self, url, soup):
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>麻瓜</h1>
        res_data =  {} #字典
        res_data['url'] = url
        title_node = soup.find('dd',class_=r"lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        # < div class ="lemma-summary" label-module="lemmaSummary" >
        summary_node = soup.find("div",class_ ="lemma-summary" )
        res_data['summary'] = summary_node.get_text()
        return res_data

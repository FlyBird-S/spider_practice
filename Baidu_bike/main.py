import html_download
import html_output
import html_parser
import url_manager

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlMannager()
        self.downloader = html_download.HtmlDownload()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_output.HtmlOutput()
    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "craw: %d,%s"%(count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 1000:
                    break
                count += 1
            except:
                print "craw error"
        self.outputer.output_html()

if __name__=="__main__":
    root_url=r"https://baike.baidu.com/item/%E7%81%AB%E5%BD%B1%E5%BF%8D%E8%80%85/8702?fr=aladdin"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
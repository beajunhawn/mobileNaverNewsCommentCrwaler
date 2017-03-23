import urllib
import requests
from bs4 import BeautifulSoup

class Crawl:
    #="<span class='u_cbox_contents' data-lang='ko'>"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
               }

    def delTag(self, tagStr, startStr):
        endPoint=0
        i=0
        while(i>len(tagStr)):
            try:
                endPoint=tagStr[len(startStr):].find('</span>')
            except:
                print("태그제거 실패")
                return;
            i+=1
        return tagStr[len(startStr):endPoint]
    def crewlHtml(self, url):
        session = requests.Session()
        r = session.get(url, headers=self.headers)
        soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
        return soup
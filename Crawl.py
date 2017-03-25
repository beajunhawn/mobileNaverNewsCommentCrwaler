import urllib
import requests
from bs4 import BeautifulSoup

class Crawl:
    #="<span class='u_cbox_contents' data-lang='ko'>"
    __abc="abc"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
               }

    #tagStr의 태그를 제거하는 메소드, startStr은 시작 태그를 endTag는 닫는 태그를 인자로 받는다.
    def delTag(self, tagStr, startStr, endTag):
        endPoint=0
        i=0
        try:
            endPoint=tagStr[int(len(startStr)):].find(endTag)#시작 태그다음 문자열 부터 닫는 태그를 찾는다.
        except Exception as e:#대체로 시작 태그나 닫는태그가 틀린경우의 오류가 대부분
            print("태그제거 실패, ")
            return;
        #print(tagStr[len(startStr):endPoint])
        return tagStr[len(startStr):len(startStr)+endPoint]

    #html을 가져와 beautifulsoup로 반환
    def crewlHtml(self, url):
        session = requests.Session()
        r = session.get(url, headers=self.headers)
        soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
        return soup
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib
import requests

from Crawler.Crawl import Crawl
from Crawler.News import News


class mnCrawler():
    catag=["politics","economy","society","it_secience","life_culture","world","entertainments","photo_section","tv_section"]
    newsLink=[]
    c=Crawl
    dom=c.crewlHtml(c, "http://m.news.naver.com/rankingList.nhn?type=section")

    def getNewsLink(self):
        return self.newsLink

    def linkCrawl(self):
        i=[]
        j=0
        for i in self.catag :
            self.besThree(self,i)

    def besThree(self, string):
        temp=1
        n="http://m.news.naver.com"
        common="body #ct div.ranking_news ul.commonlist li#"
        print(common+string+str(temp))
        while(temp<4):
            e = self.dom.select(common+string+str(temp)).pop(0).find_all("div",{"class":"commonlist_tx_headline"})
            title = self.dom.select(common+string+str(temp)+" a").pop(0)['href']
            img = n+self.dom.select("body #ct div.ranking_news ul.commonlist li#"+string+""+str(temp)+" a div.commonlist_img img")
            self.newsLink.append(News(title, e, img))
            temp+=1



'''
            e = self.dom.select("body #ct div.ranking_news ul.commonlist li#"+string+""+str(temp)+" a")
            title = self.dom.select("body #ct div.ranking_news ul.commonlist li#"+string+""+str(temp)+" a div.commonlist_tx_headline")
            img = self.dom.select("body #ct div.ranking_news ul.commonlist li#"+string+""+str(temp)+" a div.commonlist_img img")
'''

#
m=mnCrawler
m.linkCrawl(m)
i=0
for i in range(0,27):
    print(str(m.getNewsLink(m).pop(i).title)+"  !!!!!,"+str(m.getNewsLink(m).pop(i).link)+" !!!!!,"+str(m.getNewsLink(m).pop(i).imageLink)+"\n\n\n")

'''driver = webdriver.PhantomJS(executable_path='D:\\작업용 폴더\\phantomjs-2.1.1-windows\\bin\\phantomjs')
driver.get("http://m.news.naver.com/rankingRead.nhn?oid=001&aid=0009126446&sid1=100&date=20170322&ntype=RANKING")
time.sleep(7)
html=driver.page_source
soup=BeautifulSoup(html,"html.parser")
typing=soup.find_all("span",{"class":"u_cbox_contents"})
print(typing)
driver.find_element_by_class_name("u_cbox_btn_view_comment").click()
time.sleep(3)
driver.find_element_by_class_name("u_cbox_btn_more").click()
commentHtml=driver.page_source
comment=BeautifulSoup(commentHtml,"html.parser")
data=comment.find_all("span",{"class":"u_cbox_contents"})
print(data)
print()
driver.close()
'''
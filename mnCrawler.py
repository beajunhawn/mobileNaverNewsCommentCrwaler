
from bs4 import BeautifulSoup
import urllib
import requests

from Crawler.CommentCrwal import CommentCrawler
from Crawler.Crawl import Crawl
from Crawler.News import News

class mnCrawler():
    catag=["politics","economy","society","it_secience","life_culture","world","entertainments","photo_section","tv_section"] #네이버 뉴스 종류
    newsLink=[]
    c=Crawl
    dom=c.crewlHtml(c, "http://m.news.naver.com/rankingList.nhn?type=section")

    #뉴스 링크를 반환 한정자가 없기에 의미 없음
    def getNewsLink(self):
        return self.newsLink

    #리스트의 저장한 네이버 뉴스 카테고리를 순회하면서 besThree메소드를 실행함
    def linkCrawl(self):
        i=[]
        for i in self.catag :
            self.besThree(self,i)

    #네이버 뉴스의 string 인자로 받은 항목의 1위부터 3위까지의 타이틀,링크,이미지를 가저와서 News클래스에 담고 리스트에 저장하는 메소드
    def besThree(self, string):
        temp=1
        n="http://m.news.naver.com"
        common="body #ct div.ranking_news ul.commonlist li#" #네이버 뉴스가 정렬된 ul의 공통된 부모
        while(temp<4):
            #print(common+string+str(temp))
            title = self.dom.select(common+string+str(temp)).pop(0).find_all("div",{"class":"commonlist_tx_headline"})
            title= self.c.delTag(self, str(title.pop(0)),'<div class="commonlist_tx_headline">',"</div>")
            nlink = n+self.dom.select(common+string+str(temp)+" a").pop(0)['href']
            try:
                img = self.dom.select(common+string+str(temp)+" a div.commonlist_img img").pop(0)['src']
            except:
                img='이미지 없음'
            self.newsLink.append(News(title, nlink, img))
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
for item in m.newsLink:
    print("타이틀:"+str(item.title)+"  링크:"+str(item.link)+" 이미지:"+str(item.imageLink)+"\n\n\n")

#cm=CommentCrawler
#cm.commentCrawl(cm, m.newsLink.pop(0).link)
    #print(str(m.getNewsLink(m).pop(i).title)+"  !!!!!,"+str(m.getNewsLink(m).pop(i).link)+" !!!!!,"+str(m.getNewsLink(m).pop(i).imageLink)+"\n\n\n")
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
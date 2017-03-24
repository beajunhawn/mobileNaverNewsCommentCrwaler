from Crawler.Crawl import Crawl
from selenium import webdriver
import time
from bs4 import BeautifulSoup

class CommentCrawler():
    c= Crawl
    def commentCrawl(self):
        driver = webdriver.PhantomJS(executable_path='D:\\작업용 폴더\\phantomjs-2.1.1-windows\\bin\\phantomjs')
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
        return data
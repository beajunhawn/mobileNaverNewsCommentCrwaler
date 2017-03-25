from Crawler.Crawl import Crawl
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from Crawler.Comment import Comment

class CommentCrawler():
    c= Crawl
    commentList=[Comment]
    def useDriver(self, string):
        return webdriver.PhantomJS(executable_path=string)
    def commentCrawl(self, newsLink):
        driver = self.useDriver('D:\\작업용 폴더\\phantomjs-2.1.1-windows\\bin\\phantomjs')
        driver.get(newsLink)
        time.sleep(5)
        html=driver.page_source
        soup=BeautifulSoup(html,"html.parser")
        typing=soup.find_all("span",{"class":"u_cbox_contents"})
        driver.find_element_by_class_name("u_cbox_btn_view_comment").click()#코맨트 모아 보기
        time.sleep(3)
        driver.find_element_by_class_name("u_cbox_btn_more").click()#코맨트 더보기 버튼 클릭
        commentHtml=driver.page_source
        comment=BeautifulSoup(commentHtml,"html.parser")
        writer=comment.find_all("span",{"class":"u_cbox_nick"});
        print(writer)
        comments=[]
        '''for item in :
            comments.append(self.c.delTag(self.c,str(item),"<span class='u_cbox_contents' data-lang='ko'>","</span>"))
        print(comments)'''
        return comment

    def commentData(self, comment):
        #crawlTagClass=(["span","u_cbox_nick"],["span","u_cbox_contents"],["em","u_cbox_cnt_recomm"],["em", "u_cbox_cnt_unrecomm"], ["span", "u_cbox_reply_cnt"]);
        crawlTagClass=(["span", "u_cbox_nick"], ["span", "u_cbox_contents"], ["em", "u_cbox_cnt_recomm"], ["em", "u_cbox_cnt_unrecomm"]);
        commentDataList=[];
        i=0;
        item=[[str,str]];
        try:
            for tag, _class in crawlTagClass:
                a=tag
                b=_class
                havingTagStr=comment.find_all(tag,{"class" : ""+_class});
                if tag=='span' and _class=='u_cbox_contents':
                    for strlist in havingTagStr:
                        Data=self.c.delTag(self.c,str(strlist),"<"+tag+" class='"+_class+"' data-lang='ko'>", "</"+tag+">");
                        commentDataList.append(Data)
                else :
                    for strlist in havingTagStr:
                        Data=self.c.delTag(self.c,str(strlist),"<"+tag+" class='"+_class+"'>", "</"+tag+">");
                        commentDataList.append(Data);
        except Exception as e:
            print("코맨트 크롤 실패: ")

        print(commentDataList)
        return commentDataList

    def mkrCommentList(self, commentSoup):
        item=[str]
        for i in self.commentData(commentSoup):
            #오류나는 지점

            writer='';
            content='';
            goodNum='';
            badNum='';

            self.commentList.append(Comment());
        return;
'''
        writer='';
        content='';
        goodNum='';
        badNum='';
        repl='';
        writer=comment.find_all("span",{"class":"u_cbox_nick"});
        commentData=comment.find_all("span",{"class":"u_cbox_contents"});
        goodNum=comment.find_all("em",{"class":"u_cbox_cnt_recomm"});
        badNum=comment.find_all("em",{"class":"u_cbox_cnt_unrecomm"});
        repl=comment.find_all("span",{"class":"u_cbox_reply_cnt"});
'''

#
# t= CommentCrawler()
# temp= t.commentCrawl("http://m.news.naver.com/rankingRead.nhn?oid=032&aid=0002775108&sid1=100&date=20170325&ntype=RANKING")
# l=t.mkrCommentList(temp)
# print(l)
c=Crawl()
c.__
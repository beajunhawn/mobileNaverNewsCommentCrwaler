from Crawler.Crawl import Crawl
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from Crawler.Comment import Comment

class CommentCrawler():
    commentList=[Comment]
    c=Crawl
    def useDriver(self, string):
        return webdriver.PhantomJS(exec6utable_path=string)
    def commentCrawl(self, newsLink):
        driver = self.useDriver('D:\\작업용 폴더\\phantomjs-2.1.1-windows\\bin\\phantomjs')
        driver.get(newsLink)
        time.sleep(3)
        html=driver.page_source
        soup=BeautifulSoup(html,"html.parser")
        typing=soup.find_all("span",{"class":"u_cbox_contents"})
        driver
        driver.find_element_by_class_name("u_cbox_btn_view_comment").click()#코맨트 모아 보기
        time.sleep(1)
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
        templist=[];
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
                        templist.append(Data)
                else :
                    for strlist in havingTagStr:
                        Data=self.c.delTag(self.c,str(strlist),"<"+tag+" class='"+_class+"'>", "</"+tag+">");
                        templist.append(Data);
                commentDataList.append(templist)
                del(templist)
                templist=[]
        except Exception as e:
            print("코맨트 크롤 실패: "+str(e))
        print(commentDataList)
        del(templist)
        return commentDataList

    def mkrCommentList(self, commentSoup):
        list=self.commentData(commentSoup)
        print(list)
        i=0
        for i in range(0,20):
            #오류나는 지점
            writer=str(list[0][i]);
            content=str(list[1][i]);
            goodNum=str(list[2][i]);
            badNum=str(list[3][i]);
            self.commentList.append(Comment(writer,content,goodNum,badNum));
        return self.commentList;
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


t= CommentCrawler()
temp= t.commentCrawl("http://m.news.naver.com/rankingRead.nhn?oid=032&aid=0002775108&sid1=100&date=20170325&ntype=RANKING")
l=t.mkrCommentList(temp)
for i in l:
    print("작성자: "+i.commentWriter+"  내용: "+i.contents+"  좋아요: "+i.good+"  싫어요: "+i.bad)

# 결과값
# 작성자: 5284****  내용: 개인적으로  박근혜 상대로  정신적  손해배상  청구 하실분  좋아요: 8208  싫어요: 169
# 작성자: favi****  내용: 증거인멸 못하게 빨리 구속수사해라 이미 많은 증거가 인멸되었겠지만  좋아요: 6306  싫어요: 114
# 작성자: hoob****  내용: 박근혜구속 죄를지었으면 죗값을받아라  좋아요: 5678  싫어요: 104
# 작성자: leon****  내용: 어디겠노 구치소입구지  좋아요: 4977  싫어요: 97
# 작성자: ksks****  내용: 특검이 밥상 다 차려놓고 수저만 얹으면 되는데 왜 미기적거려 증거가 차고 넘친다는데...다음정권 검찰, 사법부 개혁 반드시 필요한 이유다 국민들은 분노한다 구속수사하라  좋아요: 3690  싫어요: 76
# 작성자: ceom****  내용: 무기 징역 대찬성 입니다  좋아요: 1243  싫어요: 32
# 작성자: hana****  내용: 죄를 지으면 누구나 처벌받는 대한민국을 만들자. 박근혜 구속!!!  좋아요: 1102  싫어요: 32
# 작성자: drcp****  내용: 교도소여야 하지..  좋아요: 976  싫어요: 28
# 작성자: 1004****  내용: 수사는 특검처럼~~ 아부는 검찰처럼~~ 사기는 순실이처럼~~ 거짓은 근혜처럼~~ 친일파는 완영이처럼~~ 망언은 준표처럼~~ 도망은 병우처럼~~ 모르쇠는 기춘이처럼~~ 싸가지는 유라처럼~~ 철판은 경숙이처럼~~ 뻔뻔함은 윤선이처럼~~간신은 친박처럼~~ 심부름은 국정원처럼~~ 뇌물은 삼성처럼 ~~ 몸통은 조선처럼~~ 언론은 jtbc처럼~~ 정의는 촛불처럼~~ 희망은 국민처럼~~ 모자람은 박사모처럼~~ 판결은 헌재 재판관8분처럼~~  바꾸네 감옥갈때 변기는 못들고가게 두눈뜨고 지켜봐주세요~~..썩은보수 out  좋아요: 945  싫어요: 33
# 작성자: 0174****  내용: 민간인이라면서.. 진짜 민간인 대우였으면 벌써 귀싸대기몇대 맞고 수갑차고 징역갔다...  좋아요: 843  싫어요: 28
# 작성자: girl****  내용: 죄를 짓고도 반성하고 사과할줄 모르는 철판 ... 당장 구속하라  좋아요: 734  싫어요: 23
# 작성자: suju****  내용: 죄가있다면 죄값을 받아야지 명박이랑 손잡고 교도소 가자  좋아요: 707  싫어요: 26
# 작성자: ijby****  내용: 극형을 내려도 아깝지가 않다 국가원수란것이 예의도 분수도 모르고 염병을 했다  좋아요: 676  싫어요: 27
# 작성자: auto****  내용: 박정희 무덤 파내면 안 되나요? 왜 국립묘지에 있지...  좋아요: 654  싫어요: 31
# 작성자: vlwy****  내용: 탁 탁 탁 무기징역입니다  좋아요: 601  싫어요: 30
# 작성자: guse****  내용: 감옥이 아니라 지옥불에 튀겨야할뇬~~ ^^  좋아요: 588  싫어요: 26
# 작성자: dhar****  내용: 죽어서 감옥문을 나가야지.  좋아요: 534  싫어요: 23
# 작성자: aerm****  내용: 박씨 이제 그만하시오  좋아요: 525  싫어요: 25
# 작성자: ljh2****  내용: 정말 자기밖에 모르는 그냥 공주병걸린 무능한 노처녀인데, 그걸 불쌍하다고 질질짜는 박사모를  보면 한심하다. 박사모는 자신들이 소모품이라는걸 알까? 박근혜는 자기 외에는 관심없어.  좋아요: 497  싫어요: 18
# 작성자: schw****  내용: 세월호 인양도 막았는지 조사해야 함  좋아요: 471  싫어요: 21
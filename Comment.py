class Comment:
    contents=""
    commentNum=""
    good=""
    bad=""
    commentWriter=""
    tag=""
    def __init__(self, Good, Bad, ContentsNum,  Content, writer, Tag):
        self.contents=Content
        self.good=Good
        self.bad=Bad
        self.commentNum=ContentsNum
        self.commentWriter=writer
        self.tag=Tag
    def getCommentNum(self):
        return self.commentNum
    def getGoodNum(self):
        return self.good
    def getBadNum(self):
        return self.bad
    def getTag(self):
        return self.tag
    def getContents(self):
        return self.contents
    def getCommentWriter1(self):
        return self.commentWriter
    def issuePoint(self):
        return int(self.commentNum) +int(self.good)+int(self.bad)
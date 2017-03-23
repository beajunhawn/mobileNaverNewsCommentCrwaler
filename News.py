class News:
    title=""
    link=""
    imageLink=""
    def __init__(self, Title, Link, ImageLink=None):
        self.title=Title
        self.link=Link
        self.imageLink=ImageLink
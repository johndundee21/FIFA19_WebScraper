from urllib.request import Request
from urllib.request import urlopen as Open
from bs4 import BeautifulSoup as Markup

class WebGet:
    def __init__(self, UrlPath):
        self.Path = UrlPath

    def GetRawHtml(self):
        Webpage = Request(self.Path, headers={'User-Agent': 'Mozilla/5.0'})
        RequestedPage = Open(Webpage)
        RequestedHtml = RequestedPage.read()
        RequestedPage.close()
        return Markup(RequestedHtml, "html.parser")
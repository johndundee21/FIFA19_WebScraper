import xlwt
import datetime as Date
import time
import re as StringManipulation
import os
from urllib.request import Request
from urllib.request import urlopen as Open
from bs4 import BeautifulSoup as Markup

class Time:
    @staticmethod
    def Stamp():
        TimeStamp = time.time()
        return Date.datetime.fromtimestamp(TimeStamp).strftime('%d-%m-%Y %H:%M:%S')

class WebGet:
    def __init__(self, UrlPath):
        self.Path = UrlPath

    def GetRawHtml(self):
        Webpage = Request(self.Path, headers={'User-Agent': 'Mozilla/5.0'})
        RequestedPage = Open(Webpage)
        RequestedHtml = RequestedPage.read()
        RequestedPage.close()
        return Markup(RequestedHtml, "html.parser")

class HtmlInfo:
    def __init__(self, HtmlMarkup, PlayersOnPage = 30, TableOffset = 2):
        self.HtmlMarkup = HtmlMarkup
        self.PlayersOnPage = PlayersOnPage
        self.TableOffset = TableOffset
        self.PlayerList = list()

    def Get(self, attribute):
        TableRows = self.HtmlMarkup.find_all(name = 'tr')
        for index in range(self.PlayersOnPage):
            TableData = TableRows[index + self.TableOffset].find_all('td')
            self.PlayerList.append(TableData[attribute].text)
        return self.PlayerList
    
    def ClearList(self):
        self.PlayerList.clear()
        
class Player:
    def __init__(self, playerName, playerPrice):
        self.PlayerName = playerName
        self.PlayerPrice = playerPrice

class PlayerInfo:
    def __init__(self, NameIndex = 0, RatingIndex = 1, PositionIndex = 2, PriceIndex = 4):
        self.Name = NameIndex
        self.Rating = RatingIndex
        self.Position = PositionIndex
        self.Price = PriceIndex

class Columns: 
    def __init__(self, one = 0, two = 1, three = 2):
        self.One = one
        self.Two = two
        self.Three = three

class Excel:
    def __init__(self):
        self.Book = xlwt.Workbook(encoding = "utf-8")
    
    def CreateSheet(self, SheetName):
        self.Sheet = self.Book.add_sheet(SheetName)

    def SaveSheet(self, filename):
        self.Book.save(filename + ".xls")

    

# SET CURRENT DIRECTORY AND WHERE TO PUT EXCEL FILE
CurrentWorkingDirectory = os.getcwd()
os.chdir(CurrentWorkingDirectory)

# HELPER CLASSES TO EASY MAINTAIN CODE AND READ CODE
Column = Columns()
PlayerInformation = PlayerInfo()

TotalPages = 20
CurrentPage = 1

Player = Excel()
Player.CreateSheet('Players')

for pages in range(TotalPages):
    # GET THE WEBPAGE BY URL AND GET THE RAW HTML PAGE
    Webpage = WebGet('https://www.futbin.com/players?page=' + str(CurrentPage))
    HtmlMarkup = Webpage.GetRawHtml()

    # HELPER CLASS TO FIND HTML TAGS (INITIALIZATION)
    Html = HtmlInfo(HtmlMarkup)

    PlayerNames = Html.Get(PlayerInformation.Name)

    for Index in range(Html.PlayersOnPage):
        row = Player.Sheet.row(Index + (Html.PlayersOnPage * (CurrentPage - 1)) + 1)
        Name = PlayerNames[Index]
        Name = "".join(Name.split())
        Name = StringManipulation.sub(r"(?<=\w)([A-Z])", r" \1", Name)
        row.write(Column.One, Name)

    Html.ClearList() # IF LIST IS NOT CLEARED THEN THERE WOULD NOT BE ANY NEW DATA IT WOULD BE THE SAME AS THE LAST DATA FETCHED 
    
    PlayerPrices = Html.Get(PlayerInformation.Price)

    for Index in range(Html.PlayersOnPage):
        row = Player.Sheet.row(Index + (Html.PlayersOnPage * (CurrentPage - 1)) + 1)
        Price = PlayerPrices[Index]
        Price = "".join(Price.split())
        row.write(Column.Two, Price)
    
    Html.ClearList() # IF LIST IS NOT CLEARED THEN THERE WOULD NOT BE ANY NEW DATA IT WOULD BE THE SAME AS THE LAST DATA FETCHED 

    CurrentPage += 1
    Percentages = ((CurrentPage - 1) / TotalPages) * 100
    os.system('cls')
    print("Downloading %.2f" % Percentages + "%")
    

Player.Sheet.row(0).write(Column.One, Time.Stamp())
Player.SaveSheet('FIFA')
print(Time.Stamp())


# PlayerPrices = Html.Get(PlayerInformation.Price)


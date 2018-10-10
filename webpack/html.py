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
    
    def Clear(self):
        self.PlayerList.clear()
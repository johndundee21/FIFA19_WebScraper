import os

class PageInfo:
    def __init__(self, TotalPages = 552, StartPage = 1):
        self.TotalPages = TotalPages
        self.Currentpage = StartPage
    
    def NextPage(self):
        self.Currentpage += 1
        Percentages = ((self.Currentpage - 1) / self.TotalPages) * 100
        os.system('cls')
        print("Downloading %.2f" % Percentages + "%")
    
    def PreviousPage(self):
        self.Currentpage -= 1
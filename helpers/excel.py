import xlwt
from xlutils.copy import copy
from xlrd import open_workbook
from helpers.time import Time

class ExcelWriter:
    def __init__(self):
        self.Book = xlwt.Workbook(encoding = "utf-8")
        self.Sheet = ""
    
    def CreateSheet(self, SheetName):
        self.Sheet = self.Book.add_sheet(SheetName)

    def SaveSheet(self, filename):
        self.Book.save(filename)

    def AddTimeStamp(self, column):
        self.Sheet.row(0).write(column, Time.Stamp())

class ExcelReader:
    def __init__(self, Filename, Formatting = True):
        self.Filename = Filename
        self.Formatting = Formatting
        self.Workbook
        self.ReadSheet
    
    def Open(self):
        self.Workbook = open_workbook(self.Filename, self.Formatting)
        self.ReadSheet = self.Workbook.sheet_by_index(0)

    def Copy(self):
        self.Workbook = copy(self.Workbook)

    def Sheet(self):
        return self.Workbook.get_sheet(0)
        
    def Columns(self):
        return self.ReadSheet.ncols
    
    def Rows(self):
        return self.ReadSheet.nrows
import os
import re
import openpyxl
from openpyxl import load_workbook
from helpers.file import File
from helpers.time import Time
from helpers.program import Program
from helpers.excel import ExcelWriter
from helpers.excel import ExcelReader
from helpers.string import String
from webpack.html import HtmlInfo
from webpack.url import WebGet
from futbin.player import PlayerInfo
from futbin.page import PageInfo

import xlwt
from xlutils.copy import copy
from xlrd import open_workbook
import xlsxwriter

# PROGRAM STARTS HERE

Program.SetDirectoryToCurrent()
PlayerInformation = PlayerInfo()
Page = PageInfo(TotalPages = 50)
Excel = ExcelWriter()

if not File.Exists('FIFA.xlsx'):
    Excel.CreateSheet('Players')
    Excel.Sheet.row(0).write(1, Time.Stamp())
    Excel.Sheet.col(0).width = 256 * 20
    Excel.Sheet.col(1).width = 256 * 18
    for pages in range(Page.TotalPages):

        Webpage = WebGet(f'https://www.futbin.com/players?page={Page.Currentpage}&ps_price=2000-6000000&sort=ps_price&order=desc')
        RawHtml = Webpage.GetRawHtml()
        Html = HtmlInfo(RawHtml, PlayersOnPage = 30, TableOffset = 2)

        PlayerNames = Html.Get(PlayerInformation.Name)

        for index in range(Html.PlayersOnPage):
            ExcelRow = Excel.Sheet.row(index + (Html.PlayersOnPage * (Page.Currentpage - 1)) + 1)
            ExcelRow.write(0, String.FormatToExcel(PlayerNames[index]))

        Html.Clear()
        
        PlayerPrices = Html.Get(PlayerInformation.Price)

        for index in range(Html.PlayersOnPage):
            ExcelRow = Excel.Sheet.row(index + (Html.PlayersOnPage * (Page.Currentpage - 1)) + 1)
            ExcelRow.write(1, "".join(PlayerPrices[index].split()))

        Html.Clear()
        Page.NextPage()
    Excel.SaveSheet('FIFA.xlsx')

else:
    ReadBook = open_workbook(filename='FIFA.xlsx', formatting_info=True)
    ReadSheet = ReadBook.sheet_by_index(0)
    WorkBook = copy(ReadBook)
    Worksheet = WorkBook.get_sheet(0)
    Excel.Sheet = Worksheet

    Excel.Sheet.row(0).write(ReadSheet.ncols, Time.Stamp())

    for pages in range(Page.TotalPages):

        Webpage = WebGet(f'https://www.futbin.com/players?page={Page.Currentpage}&ps_price=2000-6000000&sort=ps_price&order=desc')
        RawHtml = Webpage.GetRawHtml()
        Html = HtmlInfo(RawHtml, PlayersOnPage = 30, TableOffset = 2)

        PlayerPrices = Html.Get(PlayerInformation.Price)

        for index in range(Html.PlayersOnPage):
            ExcelRow = Excel.Sheet.row(index + (Html.PlayersOnPage * (Page.Currentpage - 1)) + 1)
            ExcelRow.write(ReadSheet.ncols, "".join(PlayerPrices[index].split()))

        Html.Clear()
        Page.NextPage()
    Excel.Sheet.col(ReadSheet.ncols).width = 256 * 18
    WorkBook.save('FIFA.xlsx')


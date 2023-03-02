import requests as req
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook
import time

workbook = Workbook()
sheet = workbook.active

for i in range(30000, 40000):
    params = {'contentId': i}


    url = 'https://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do'
    html = req.get(url, headers={'User-Agent': 'Mozilla/5.0'}, params=params).text
    #print(html)

    dom = bs(html, 'html.parser')

    lis = dom.select('#content > div.healthinfoWrap.clearfix > div.regionReviewLeft > div.otherRegionBox > ul > li')
    for li in lis:
        contBox = li.select_one('div.contBox')
        title = contBox.select_one('strong.contTitle').text #병명
        depts = contBox.select('dl > dd:nth-child(6) > a')  #관련 과들

        if title != None:
            text =[title] 

            for dept in depts:
                text.append(dept.text)

            sheet.append(text)
            print(text)

workbook.save('C:\\Users\\user\\Desktop\\crawling.xlsx')
workbook.close()

print('프로그램 종료')
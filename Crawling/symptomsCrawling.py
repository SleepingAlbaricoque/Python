import requests as req
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook
import time

workbook = Workbook()
sheet = workbook.active

symptomId = 'SS00000'

for i in range(1, 10):
    if i >= 10 and i < 100:
        symptomId = 'SS0000'

    if i >= 100 :
        symptom = 'SS000'

    params = {'symptomIds' : symptomId + str(i)}

    url = 'https://www.amc.seoul.kr/asan/healthinfo/symptom/symptomList.do'
    html = req.get(url, headers={'User-Agent': 'Mozilla/5.0'}, params=params).text

    dom = bs(html, 'html.parser')
    symptom = dom.select_one('#content > div.healthinfoWrap > div.selectTypeBox > dl > dd').text

    if symptom != None:
        text =[symptom]

    for j in range(1, 10):
        params = {'symptomIds' : symptomId + str(i), 'pageIndex' : j}

        url = 'https://www.amc.seoul.kr/asan/healthinfo/symptom/symptomList.do'
        html = req.get(url, headers={'User-Agent': 'Mozilla/5.0'}, params=params).text
        #print(html)

        dom = bs(html, 'html.parser')

        lis = dom.select('#listForm > div > div > ul > li')
        liSize = len(lis)
        counter = 0

        for li in lis:
            contBox = li.select_one('div.contBox')
            illness = contBox.select_one('strong.contTitle > a') #병명

            if illness != None:
                text.append(illness.text)          

    sheet.append(text)
    print(i, j, text)

workbook.save('C:\\Users\\java1\\Desktop\\symptoms.xlsx')
workbook.close()

print('프로그램 종료')
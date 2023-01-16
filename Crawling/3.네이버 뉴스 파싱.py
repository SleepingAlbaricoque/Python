"""
날짜 : 2023.01.16
이름 : 조수빈
내용 : 파이썬 웹사이트 크롤링 및 파싱 실습하기
"""

import requests as req
from bs4 import BeautifulSoup as bs
from openpyxl import workbook
import time

# HTML 요청
url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230'

html = req.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text # 정상적인 요청은 브라우저를 통해서; 지금은 프로그램(파이썬)을 통해서 요청하는 것이므로 네이버 서버가 이러한 요청을 악성코드로 간주하여 차단함 => request 요청 할 때(get 함수 쓸 때) headers={'브라우저 엔진'} 매개변수로 주면 우회 가능
#print(html)

# 문서 객체 생성
dom = bs(html, 'html.parser')
tit = dom.select_one('#main_content > div.list_header.newsflash_header > h3').text
print('tit: ', tit)

lis = dom.select('#main_content > div.list_body.newsflash_body > ul > li') # 원래 복사한 선택자는 #main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(1)이었는데 list의 모든 요소 가져오기 위해 ul, li 뒤의 선택자 각각 삭제
for li in lis:
    title = li.select_one('dl > dt:not(.photo) > a').text # dt가 두 개 인데 하나는 클래스 이름 photo로 돼있음 -> photo 아닌 dt 선택하기 위해 not 사용
    print('title: ', title.strip()) # strip은 자바 trim()과 동일한 기능
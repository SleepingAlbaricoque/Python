"""
날짜 : 2023.01.16
이름 : 조수빈
내용 : 파이썬 HTML 파싱(추출) 실습하기
"""

import requests as req
from bs4 import BeautifulSoup as bs

# 파싱할 페이지(HTML) 요청
url = 'http://chhak.click/parsing/sample2.html'
html = req.get(url).text
print(html)


# 문서 객체 생성
dom = bs(html, 'html.parser')

# 문서 파싱
tit = dom.html.body.h1.text # text는 jQuery 내용 함수
txt = dom.select_one('p').text
lis = dom.select('ul > li') # 말 그대로 list라는 뜻
print(tit)
print(txt)
for li in lis: 
    print('li text: ', li.text)

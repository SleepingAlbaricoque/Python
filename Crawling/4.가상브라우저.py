"""
날짜 : 2023.01.17
이름 : 조수빈
내용 : 파이썬 가상브라우저 실습하기; js 이용해 동적으로 화면 구현하는 웹사이트의 경우 기존 방식으로 파싱 불가 => 가상 브라우저 필요
"""

# pip install selenium
# 웹에서 chromedriver 검색 > WebDriver for Chrome 다운(현재 크롬 버전 체크 후 맞는 걸로)
# chromedriver.exe 파일 파이썬 Crawling 폴더로 복붙하기

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 가상브라우저 실행
chrome_options = Options()
chrome_options.add_experimental_option("detach", True) # 창 자동 꺼짐 방지 위한 코드

browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

# 네이버 이동
browser.get('https://naver.com')

# 로그인 버튼 클릭
btnLogin = browser.find_element(By.CSS_SELECTOR, '#account > a')
btnLogin.click()

# 아이디/비번 입력
input_id = browser.find_element(By.CSS_SELECTOR, '#id')
input_pw = browser.find_element(By.CSS_SELECTOR, '#pw')
input_id.send_keys('abcd')
input_pw.send_keys('1234')

# 최종 로그인 클릭
btnSubmit = browser.find_element(By.CSS_SELECTOR, '#log\.login')
btnSubmit.click()
"""
날짜 : 2023.01.12
이름 : 조수빈
내용 : 파이썬 외부패키지모듈 실습하기

패키지 설치 예시
pip install openpyxl
"""

# command 'pip' for downloading package modules 
# ex.pip install openpyxl - download excel for python

from openpyxl import Workbook # workbook = excel sheet

# 새로운 엑셀 파일 생성
workbook = Workbook()

# 현재 시트 활성화
sheet = workbook.active

# 데이터 입력
sheet['A1'] = '파이썬 Excel 실습'
sheet.append(['아이디', '이름', '휴대폰', '나이', '주소'])
sheet.append(['a101', '김유신', '010-1234-0001', '23', '김해시'])
sheet.append(['a102', '김춘추', '010-1234-0002', '31', '경주시'])
sheet.append(['a103', '장보고', '010-1234-0003', '33', '완도시'])

# 저장 종료
workbook.save('C:/Users/java1/Desktop/Member.xlsx')
workbook.close()

print('프로그램 종료')



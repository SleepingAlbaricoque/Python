"""
날짜 : 2023.01.11
이름 : 조수빈
내용 : 파이썬 상속 실습하기
"""

from sub2.StockAccount import StockAccount

kb = StockAccount('KB증권', '102', '홍길동', 50000, '삼성전자', 10, 60000)
kb.deposit(1000000)
kb.sell(5, 70000)
kb.show()

"""
날짜 : 2023.01.11
이름 : 조수빈
내용 : 파이썬 클래스 실습하기
"""
from sub1.Car import Car # 직접 임포트 선언해야 함
from sub1.Account import Account

bmw = Car('BMW', '검정색', 5000)
bmw.speedUp()
bmw.speedDown()
bmw.show()

sonata = Car('소나타', 'white', 3000)
sonata.speedUp()
sonata.speedDown()
sonata.show()

kb = Account('국민', '123', '김수한무', 10000)
kb.deposit(40000)
kb.withdraw(5000)
kb.show()

wr = Account('우리', '324', '김김김', 10000)
wr.deposit(40000)
wr.withdraw(5000)
wr.show()

# 캡슐화: 직접 참조 못하게; 파이썬에는 접근 제한 지시자가 없음 => 언더바 처리

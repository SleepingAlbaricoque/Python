"""
날짜 : 2023.01.11
이름 : 조수빈
내용 : 파이썬 모듈(객체) 실습하기
"""
import sub2.calc # 밑에서 쓸 때 sub2.calc 풀네임으로 사용해야 함
import sub2.calc as c
from sub2.calc import * # 밑에서 쓸 때 함수이름만 가지고 사용 가능

r1 = c.plus(1, 2)
print('r1: ', r1)

r2 = c.minus(1, 2)
print('r2: ', r2)

r3 = c.multi(1, 2)
print('r3: ', r3)

r4 = c.div(4, 2)
print('r4: ', r4)



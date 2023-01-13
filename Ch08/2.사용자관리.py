"""
날짜 : 2023.01.13
이름 : 조수빈
내용 : 파이썬 사용자관리 실습하기
"""
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                user='root',
                password='1234',
                db='java1db',
                charset='utf8')

cur = conn.cursor()

while True:
    print('0: 종료, 1: 등록, 2: 조회, 3: 검색, 4: 삭제')
    answer = 0

    try:
        answer = int(input('선택: '))
    except Exception as e:
        print('다시 입력하세요', e)
        continue

    if answer == 0:
        break
    elif answer == 1:
        data = list(input('가입할 회원 정보를 입력하세요: 아이디, 비밀번호, 이름, 전화번호, 나이: ').split())
        print(data)
        sql = "insert into `user1` values ('%s', '%s', '%s', '%s', '%d')" 
        cur.execute(sql % (data[0], data[1], data[2], data[3], int(data[4])))
        conn.commit()
    elif answer == 2:
        user = cur.execute("select * from `user1`;")
        conn.commit()

        print('|아이디|비번|이름|휴대폰|나이|')
        for row in cur.fetchall():
            print('--------------------')
            print('|%s|%s|%s|%s|%d|' % (row[0], row[1], row[2], row[3], row[4]))
            
        print('조회 완료')
    elif answer == 3:
        name = input('조회할 회원의 이름을 입력하세요: ')
        user = cur.execute("select * from `user1` where `name`='{}'".format((name)))
        conn.commit()

        print('|아이디|비번|이름|휴대폰|나이|')
        for row in cur.fetchall():
            print('--------------------')
            print('|%s|%s|%s|%s|%d|' % (row[0], row[1], row[2], row[3], row[4]))
            
        print('검색 완료')
    elif answer == 4:
        print('삭제하실 회원의 아이디를 입력하세요')
        answer = input('아이디: ')
        sql = "delete from `user1` where `uid`='" + answer + "';"
        cur.execute(sql)
        conn.commit()
        print('삭제되었습니다')
    else:
        print('0에서 4 중에 입력하세요')
        continue

# DB 종료
conn.close()

# 프로그램 종료
print('프로그램 종료')
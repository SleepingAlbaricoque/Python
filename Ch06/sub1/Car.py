class Car:

    # 생성자
    def __init__(self, brand, color, price): 
        # 속성
        self.brand = brand
        self.color = color
        self.price = price


    # 기능
    def speedUp(self): # 멤버 함수라 매개변수자리에 self 지시자를 넣어서 멤버 함수임을 마크
        print('%s 속도 올리기' % self.brand)

    def speedDown(self):
        print('%s 속도 내리기' % self.brand)

    def show(self):
        print('차량명: ', self.brand)
        print('차량색: ', self.color)
        print('가격: ', self.price)
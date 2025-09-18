# self 
class multiply1:
    # 멤버 변수
    # 생성자 생략시 :묵시적(default) 생성자
        # def __init__(self):
        #     pass

    # 동적 멤버변수 생성/초기화
    def data(self, x,y):
        self.x = x
        self.y = y

    # 곱셈 연산 함수
    def mul(self):
        result = self.x * self.y
        self.display(result)

    def display(self, result):
        print("곱셈 결과: %d" % result)

obj = multiply1()
obj.data(10,20)
obj.mul()

#

# 클래스와 객체
class calc_class:
    # 클래스 변수 => 자료 저장
    x = y = 0

    # 생성자: 인자가 있는 생성자
    def __init__(self,a,b):
        self.x = a
        self.y = b

    # 클래스 함수
    def plus(self):
        p = self.x + self.y
        return p
    
    def minus(self):
        m = self.x - self.y
        return m

# 객체 생성
myObj = calc_class(10,20)
print(myObj.plus())
print(myObj.minus())

myObj2 = calc_class()


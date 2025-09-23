
class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name

    def pay_calc(self): # 추상 클래스
        pass

class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name) # name 부모 자원 -> 부모 생성자통홰 초기화

    def pay_calc(self, base, bonus): # 오버라이딩
        self.pay = base+bonus
        print('총 수령액: ', format(self.pay, '3,d'),'원')

class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, tpay, time):
        self.pay = tpay * time
        print('총 수령액: ', format(self.pay, '3,d'),'원')

p = Permanent("홍길동")
p.pay_calc(3000000, 200000)

t = Temporary("김길동")
t.pay_calc(15000, 80)


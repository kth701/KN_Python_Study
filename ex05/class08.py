#다형성: 여러가지 형태를 가질 수 있는 능력

# 부모 클래스(베이스 클래스)
class Flight:
    def fly(self):
        print('날다, fly원형 메서드')

class Airplane(Flight):
    # 재정의 -> 오버라이딩
    def fly(self):
        print('비행기가 날다')

class Bird(Flight):
    def fly(self):
        print('새가 날다')

class PaperAirplane(Flight):
    def fly(self):
        print('종이 비행기가 날다')


# 객체 생성
# 부모 클래스로 생성한 객체
flight = Flight()

air = Airplane() 
bird = Bird()
paper = PaperAirplane()

# 다형성
flight.fly() # 날다

flight = air # 묵시적(암시적, 자동)형 변환
flight.fly() # 비행기 날다

flight = bird
flight.fly()

flight = paper
flight.fly()



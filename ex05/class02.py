class Car:
    # 멤버변수
    cc = 0 # 엔진
    door = 0 # 문짝
    carType = None # null  # 승용, SUV, 트럭

    # 생성자
    def __init__(self, cc, door, carType):
        # 멤버 변수 초기화
        self.cc = cc
        self.door = door
        self.carType = carType
    
    #  함수
    def display(self):
        print("자동차는 %d cc 이고, 문짝은 %d 개이며, 타입은 %s 입니다." % (self.cc, self.door, self.carType))

# 객체 생성
myCar1 = Car(3000, 4, "SUV")
myCar1.display()
myCar2 = Car(2000, 5,"SUV")
myCar2.display()


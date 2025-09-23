# 클래스 멤버 :  클래스 이름으로 호출할 수 있는 클래스 변수와 클래스 메서드
# 클래스 메서드: cls라는 기본인수를 사용, @classmethod라는 함수 장식자를 이용하여 선언

class DataPro:
    # 클래스 변수
    content = "날짜 처리 클래스"

    def __init__(self, year, month, day):
        # 멤버 변수
        self.year = year
        self.month = month
        self.day = day

    #멤버 메서드
    def display(self):
        print("오늘은 %d년 %d월 %d일 입니다." % (self.year, self.month, self.day))

    # 클래스 메서드(class method)
    @classmethod
    def date_string(cls, date_str):
        year = int(date_str[0:4])
        month = int(date_str[4:6])
        day = int(date_str[6:8])
        return cls(year, month, day) # 생성자 호출
    
# 객체 생성
date = DataPro(2025,9,18) # 생성자 호출
print(date.content) # 날짜 처리 클래스
print(date.year) # 2025
print(date.month) # 9
print(date.day) # 18

date.display() # 오늘은 2025년 9월 18일 입니다.

#객체 생성없이 클래스 변수, 클래스 메서드 호출
# 클래스 멤버
print(DataPro.content) # 날짜 처리 클래스
# print(DataPro.year) # AttributeError: type object 'DataPro' has no attribute 'year'
DataPro.date_string("20240918") # 생성자 호출
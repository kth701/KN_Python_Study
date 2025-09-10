# 표준 입력(키보드)출력(콘솔) 장치

# 문자형 숫자 입력
num = input("숫자입력(str): ") # 키보드 통해 데이터 입력받아 메모리 변수에 할당
print(num, num*5) # 문자열로 처리
print(type(num))

#  문자형 숫자를 숫자형으로 변환: str -> int
num2 = int(input("숫자입력(int): "))
print(num2, num2*5)
print(type(num2))

num3 = float(input("숫자입력(float): "))
print(num3, num3*5)



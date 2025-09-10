# 변수 : 단일 기억장소 -> 변수 선언시  타입 구분 안함
# 자료형 :

var1 = "Hello World"
print(var1)
print(type(var1)) # 자료형 타입 추출


var2 = '홍길동'
print(type(var2))

var3 = 100
print(type(var3))

var4 = 150.25
print(type(var4))

var5 = True # True, False
print(type(var5))

print(id(var1)) # 변수의 메모리 주소를  10진로 환산해서 표시
print(id(var2))
print(id(var3))
print(id(var4))
print(id(var5))  

# 예약어 확인
import keyword
print(keyword.kwlist)










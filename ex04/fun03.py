
# 사용자 정의 함수
#  def 함수명(매개변수):
#     실행문
#     return 반환값

print("-"*10)
# 인수가 없는 함수
def userFunc1():
    print('인수가 없는 함수')
    print("나는 userFunc1()함수 입니다.")

# 함수 호출
userFunc1()
print("-"*10)

#  인자가 있는 함수
def userFunc2(a, b):
    print('userFunc2() 함수')
    add = a + b
    return add

rs = userFunc2(10, 20)
print(rs)

print("-"*10)
def userFunc3(a, b):
    print('userFunc3() 함수')

    add = a + b
    sub = a - b
    mul = a * b
    div = a / b

    return add, sub, mul, div

a,b,c,d = userFunc3(10, 20)
print(a,b,c,d)
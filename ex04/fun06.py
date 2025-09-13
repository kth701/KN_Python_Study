# 스코프(scope)
x = 50 # 전역변수 (함수 밖
def local_func(x):
    x += 50 # 지역변수 (함수 안)
    print('local_func(x) => ', x)

local_func(x)
print(x) # 전역 변수

# global
def global_func():
    global x #  전역변수 x을 지칭
    x += 50

global_func()
print(x)
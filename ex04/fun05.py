# 람다 함수
# 일반 함수
def Adder(x,y):
    add = x + y
    return add

print(Adder(10,20))

# 람다 함수 
print("-- lambda함수")

rs = (lambda x, y : x+y)(100,200)
print(rs)

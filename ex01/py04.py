# 대입 연산자 활용
# 변수: 단일 기억장소, 배열=여러개의 기억장소
i = 0
print(i) # 0

i = i + 1 # 1추가-> 1
print(i)

i = i + 1
print(i) # 2

i = i + 1 # 1추가
print(i) # 3

# += , -=, *= , /=, %=
i += 1
print(i) # 4

j = 100
print(j)

j -= 10
print(j) # 90

j *= 2
print(j) # 180

print("-"*5, "누적")
a = 0
b = 0

a += 1 # a=1
b += a # b=1
print(a, b)

a += 1 # a=2
b += a # b=(1)+2
print(a, b)

a += 1 # a=3
b += a # (1+2) + 3
print(a, b)

a += 1 # a=4
b += a # (1+2+3) + 4
print(a, b)

print("Hello", end="-")
print("World")

print("-"*5,"변수 교체")
a = 100
b = 200
print(a, b)

a, b = b, a
print(a, b)

t=a
a=b
b=t
print(a, b)

# 여러개의 값을 묶어서 변수에 할당하는 연산자
print("-"*5,"패킹 할당")
lst = [1,2,3,4,5]
print(lst)
print(type(lst))

v1, *v2 = lst
print(v1, v2)

*v1, v2,v3 = lst
print(v1, v2, v3)

v1, *v2, v3 = lst
print(v1, v2, v3)








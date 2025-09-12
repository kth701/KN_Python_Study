# 리스트 연산자: "+"결합, "*" 확장

x = [1,2,3,4]
y = [1.5, 2.5]

z = x + y #  new object
print(x,y, z)

# 리스트 확장
x.extend(y)
print(x)


# 리스트 추가
x.append(y)
print(x)
print(x[0], x[1], x[2], x[3], x[4],x[5],x[6] )
print(x[6][0], x[6][1])

# "*" 반복확장
lst = [1,2,3,4]
result = lst * 3
print(result)

# 리스트 요소 검사
result.sort()
print(result)

result.sort(reverse=True)
print(result)


import random
r = []
# for 루프의 반복 변수 'r'이 리스트 'r'을 덮어쓰는 문제를 해결하기 위해 반복 변수를 'i'로 변경합니다.
for i in range(10):
    # print(i)
    num = random.randint(1,5)
    # print(num, type(num))

    r.append(num)

# 루프가 끝난 후 생성된 리스트를 출력합니다.
print(r)

if 41 in r: # r객체에 4포함되어 있으면 true
    print('있음')
else:
    print('없음')
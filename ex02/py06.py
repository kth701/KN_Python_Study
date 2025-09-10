# 중복 for
import random

print("-"*10)
print( 9 in [1,2,3,4,5])
print("-"*10)


# 리스트 구조안에 리스트 선언 => 2차원 배열구조 형성
list1 = [
    [], # 0행 0열,1열, 2열,....
    [], # 1행 0열,1열, 2열,....
    [],
    [],
    []
]

for  outer in range(5): # 0-4까지

    # inner for 반복 시작
    for inner in range(6): # 0-5까지
        r = random.randint(1,45) # 1-45사이 난수 발생
        
        # 난수 발생후 저장소에 유무 체크
        while r in list1: # r값이 list1에 있으면 반복수행
            r = random.randint(1,45)
        
        list1[outer].append(r) # 리스트에 저장 => list1[0][0], [0][1],... [0][5],  list1[1][0],....
        print(r, end=" ")

        # inner for 반복 끝

    print() # 줄바꿈

print("-"*10)
for i in range(5):
    print(list1[i])

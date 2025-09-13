# Set: 비순차 자료구조. {}중괄호
# 중복 허용하지 않음, index없음, 추가,삭제 및 집합 연산 등 가능

# 중복 불가
s1 = {1,3,4,3,1}
print(s1, len(s1))
print(type(s1))

for d in s1: # {1,3,4}
    print(d, end=' ')
print()

# 집합 연산
s2 = {3,6}
print(s1, s2)
print( s1.union(s2)) # 합집합
print(s1.difference(s2)) #  차집합
print(s1.intersection(s2)) # 교집합

# 추가, 삭제
s3 = {1, 3, 5}
print(s3)

s3.add(7) # 원소 추가
print(s3)

s3.discard(3) # 원소 삭제
print(s3)

s3.clear() # 모든 원소 삭제
print(s3) 

# 중복 원소 제거
gender=['남','여','여','남','여','남','여']
print(gender)

sgender=set(gender) # list -> set -> 중복제거
print(sgender) # {'여', '남'}

gender=list(sgender) # set -> list
print(gender) # ['여', '남']
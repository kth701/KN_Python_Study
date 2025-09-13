# 객체 주소 복사
name = ['홍길동', '이순신', '강감찬']
print(name, id(name))

name2 = name # name의 주소를 name2에 저장
print(name2, id(name2))

name2[0] = '동길이홍'
print(name, name2)

import copy
name3 = copy.deepcopy(name) # 깊은 복사( 내용: 데이터 복사)
name2[0] = '김길동'

print(name, name2, name3)
print(id(name3))
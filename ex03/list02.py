# list 객체에 추가,삭제, 수정, 삽입

num = ['one','two', 'three', 'four']
print(num, len(num))

# 추가
num.append('five') # 기존 데이터 마지막에 위치
print(num)

# 삭제
num.remove('five')
print(num)


# 삽입
num.insert(0, 'zero')
print(num)

# 수정
num[3] = '4'
print(num)

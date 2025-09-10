# 문자열 처리 함수
oneLine = "this is one line string"
print('글자수: ', len(oneLine))

# 특정 문자 비교 판단
print(oneLine.startswith('this')) # 시작하는 문자열 있으면 True
print(oneLine.startswith('is')) # 시작하는 문자열이 없으면 False

#  특정 문자 포함 여부
print("-"*5, 'in 사용하기')
print("안녕" in "홍길동님 안녕하세요") #  True
print("김길순" in "홍길동님 안녕하세요") # False
print( 1 in [1,2,3,4,5]) # True
print( 10 in [1,2,3,4,5]) # False
print( [1] in [1,2,3,4,5, [1], [1,2]  ]) # True =>[1] 리스트가 포함

# 특정 문자 교체 -> 특정 문자 제거할 때 많이 사용
# print(oneLine.replace('this', 'that'))
oneLine = oneLine.replace('this', 'that')
print(oneLine)

print(oneLine.replace(" ", "/"))

#  문자열 분리
str1 = """\
this is
multi line
동길님 안녕하세요
김길동 반가워요\
"""
print(str1)

str2 = str1.split('\n') # '\n' 문자 기분으로 분리하여 리스트 구조로 저장
print(str2, type(str2), '문장: ' ,len(str2))

str3 = str2[0].split(' ')
print(str3, type(str3), '단어: ' ,len(str3))

# 문자열 결합
print("-"*5)
print(str3, type(str3))

str_join = ','.join(str3)
print(str_join, type(str_join))

# 이스케이프 문자 기능 및 차단
names='홍\길동\n홍길순\n동길이\n동\순이'
print(names)

path_name = "c:\\windows\\abc\\uploads\\"
print(path_name)

# path = "c:\\windows\\temp\\downs"
# print(path)



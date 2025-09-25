# 정규식 표현 
# re모듈 import할 것


#문자열 찾기
from re import findall


st1 = '1234 abc홍길동 ABC_555_6 이사도시'


# 숫자 찾기
# print(findall('1234', st1))
# print(findall('[0-9]', st1))
# print(findall('[0-9]{3}', st1))# x{n}-> x가 n번
# print(findall('[0-9]{3,}', st1))# x{n,}-> x가 n번이상
# print(findall('\\d{3,}', st1)) # '\d'

# 특정 위치의 문자열 찾기
# st2 = 'test1abcABC 123mbc  45test'
# print(st2)

# 접두어/접미어
# print(findall('^test', st2))
# print(findall('st$', st2)) # 'st로 끝나는 문자열'

# print(findall('.bc',st2)) # 한문자 와일드 문자
# print(findall('t.', st2))

st3 = 'test^홍길동 abc 대한*민국 123$tbc'
words = findall('\\w{3,}', st3) # 문자 또는 숫자를 의미, [a-zA-Z0-9]와 동일
print(words)

words2 = findall('[^^*$+]',st3) # 특수문자 제외
print(words2)
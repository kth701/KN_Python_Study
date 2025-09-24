# 정규식 표현 
# re모듈 import할 것


#문자열 찾기
from re import findall

st1 = '1234 abc홍길동 ABC_555_6 이사도시'


# 숫자 찾기
print(findall('1234', st1))
print(findall('[0-9]', st1))
print(findall('[0-9]{3}', st1))
print(findall('[0-9]{3,}', st1))
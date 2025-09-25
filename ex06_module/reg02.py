# from re import match
import re

# 패턴과 일치된 경우
# jumin = '123456-9234567'
# result = re.match('[0-9]{6}-[1-4][0-9]{6}', jumin) # true/null 판별
# print(result)

# if result:
#     print('주민번호형식 정상')
# else: #None
#     print('잘못된 주민번호 형식입니다.')


from re import sub, split, match, compile
# 문자열 치환
# st3 = 'test^홍길동 abc 대한*민국 123$tbc'

# 특수문자 제거
# print("- 특수문자 제거하기 -")
# text1 = sub('[\^*$]+', '', st3) # sub('문자','치환될문자', 대상문자열)
# print("st3:",st3)
# print("제거후:",text1)

# 테스트 자료
multi_line = """\
http://www.naver.com
http://www.google.com
www.daum.net\
"""
print(multi_line)

# 구분자를 이용하여 문자열 분리
web_site = split("\n", multi_line)
print(web_site)

# 패턴 객체 만들기
pat = compile("http://")

sel_site = [ site for site in web_site if match(pat, site)]
print(sel_site)

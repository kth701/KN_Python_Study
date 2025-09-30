# 자연어 전처리
from re import findall, sub

# 더미 텍스트
texts = [
' 우리나라 대한미국., 우리나라%$ 만세',
'비타민&라 100GRAM 분량',
'나는 대한민국 사람인가?',
'보험료 15000원에 평생 보장 마감 임박!!!',
'나는 길김동***'
]

print('원본:')
print(texts)
print('-'*20)

# 텍스트 전처리 함수
def crean_text(text):
    #1-6단계 처리
    texts_re1 = text.lower()
    texts_re2 =  sub('[0-9]','', texts_re1 )
    texts_re3 = sub('[,.?!:;]','', texts_re2)
    texts_re4 = sub('[@#$%^&*]','', texts_re3)
    texts_re5 = sub('[a-z]','', texts_re4)
    texts_re6 = ' '.join(texts_re5.split())

    return texts_re6

# 함수 호출
texts_result = [crean_text(text) for text in texts]
print(texts_result)




# 1단계; 소문자 변경
# texts_re1 = [t.lower() for t in texts]
# print('1단계')
# print(texts_re1)
# print('-'*20)

# # 2단계 : 숫자 제거
# texts_re2 = [ sub('[0-9]','', text ) for text in texts_re1]
# print(texts_re2)
# print('-'*20)

# # 3단계: 문장부호 제거
# texts_re3 = [ sub('[,.?!:;]','', text) for text in texts_re2]
# print(texts_re3)
# print('-'*20)

# # 4단계: 특수문자제거
# texts_re4 = [ sub('[@#$%^&*]','', text) for text in texts_re3]
# print(texts_re4)
# print('-'*20)


# # 5단계: 영문문자제거
# texts_re5 = [ ''.join(findall('[^a-z]', text)) for text in texts_re4]
# print(texts_re5)
# print('-'*20)

# # 6단계: 공백문자제거
# texts_re6 = [ ' '.join(text.split()) for text in texts_re5]
# print(texts_re6)
# print('-'*20)
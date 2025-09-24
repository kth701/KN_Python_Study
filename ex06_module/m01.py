# 내장 클래스: builtins 모듈 => 별도의 호출 없이 바로 사용
# import 모듈 => 반드시 호출

# 리스트 열거형 객체 이용
lst = [1,3,5]
for i,c in enumerate(lst):
    print('index:',i, end=',')
    print('data:', c)

print()

# 튜플 열거형
dit = {'name':'홍길동', 'job':'회사원', 'addr': '창원시'}
for i, k in enumerate(dit):
    print('순서:', i, end=', ')
    print('키',k, end=', ')
    print('값:', dit[k], dit.get(k))


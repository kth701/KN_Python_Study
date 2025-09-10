# 자료구조 : 데이터(객체)가 메모리에 배정될 때 기억공간에 적재되는 구조
# 순서 자료구조:  리스트, 스트링(문자열),..
# 비순서 자료구조:  딕셔너리,..

# str 클래스 형식
# str_var = str(object='.') # str_var = '홍길동 문자열입니다.'
# print(str_var)
# print(type(str_var))
# print(str_var[0], str_var[1], str_var[-1])


# 리스트=> 대괄호[] 안에 콤마(,)를 이용
# 변수 = [값1,....]
# index가 있음,  슬라이싱, 연결, 반복, 요소 검사 등 가능
# 값을 추가, 삭제, 수정, 삽입 가능

# 단일 list
lst = [0,1,2,3,4,5,6,7,8,9]
print(lst)
print(type(lst))

for i in lst:
    print(i, end=' ')

print()
# 슬라이싱
# print(lst[0:9])
# print(lst[:5]) # 0~4
# print(lst[5:], lst[5:9])
# print(lst[::])
# print(lst[::2])

# print(lst[::-1])
# print(lst[5:-1])

# 중첩 list
a = ['a','b','c']
b = [10,20, a, 5, True, '문자열'] # 서로 다른 자료형 허용
# print(a)
# print(b)
print(b[0], b[1])
print(b[2], b[2][0], b[2][1], b[2][2])
print(b[2][1:])




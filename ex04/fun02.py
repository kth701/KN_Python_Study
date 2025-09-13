# builtins모듈에 있는 내장함수

# shift+Enter => python shell실행 상태
abs(10)
abs(-10)
abs(-10.54)
#  모든 요소가 True -> True 판별
all([1,2,3]) # 숫자 0만 False, 나머지 숫자 모두 True
all([1,2,3,0])
all([1, True, -10,"홍길동", [1,2,3], (10,), {12,2}, {'k':'100'}])
all([1, True, -10,"홍길동", [], (10,), {12,2}, {'k':'100'}])

# any: 하나 이상의 요소가  True ->  True
any([0,False,[]])
any([0,False,[1]])

bin(10)
hex(10)
oct(10)

eval("10+20") # 문자열 수식 -> 계산식 수식
ord('A') # 문자 -> 아스키 코드
ord('a')
ord('a') -ord('A')

chr(65) # 코드 -> 아스키 문자

pow(2,3)
round(3.141592)
round(3.141592,4)

sorted([3,2,1,5])
sorted([3,2,1,5], reverse=True)

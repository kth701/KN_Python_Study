# 리스트 내포
# 변수 = [실행문 for 변수 in 열거형 객체
# 변수 =[조건결과가 참인 경우만 실행문 for 변수 in 열거형 객체 if 조건]

x = [2,4,1,5,7]
print(x)
# print(x**2) # error
lst = [x**2 for x in x]
print(lst)

num = list(range(1, 11))
print(num)

lst2 = [ i*2 for i in num if i%2 == 0 ]
print(lst2)



# 튜플(Tuple): 리스트 구조와 유사, 읽기 전용(수정, 삭제 불가)
# 변수 = (값1,...)
# 인덱스, 슬라이싱, 연결, 반복, 요소검사 등 가능
# 리스트 보다 처리 속도가 빠르다
t1 = (10,) # lst1 = [10]
test = (10)
print(t1, type(t1), test, type(test))

t2 = (1,2,3,4,5)
print(t2)

print(t2[0])
print(t2[1:4])
print(t2[-1])
# t2[0] = 100 # error

if 6 in t2:
    print('있음')
else:
    print('없음')

# 튜플 자료형 변환
lst = list(range(1,6)) # range -> list
print(lst)

t3 = tuple(lst) # list -> tuple
print(t3, type(t3))
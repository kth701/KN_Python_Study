# 재귀 함수
def counter(n):
    print(n,'번째')
    if n == 0:
        return 0
    else:
        return counter(n-1)

counter(3)
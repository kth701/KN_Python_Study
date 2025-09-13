# 가변인자 : 기호 => "*", "**"

# 튜플형 가변인자
def fun_01(name, *names):
    print(name)
    print(names) # 튜플 (리스트 구조와 유사)
    print(names[0], names[:2])

fun_01("홍길동", "이순신","길동길","강감찬")

# import, *가변인자
from statistics import mean, variance, stdev

def statis(func, *data):
    if func == 'avg':
        return mean(data)
    elif func == 'var':
        return variance(data)
    elif func == 'std':
        return stdev(data)
    else:
        return 'TypeError'
    
# statis함수 호출
print('avg=', statis('avg', 1,2,3,4,5))
print('var=', statis('var', 1,2,3,4,5))
print('std=', statis('std', 1,2,3,4,5))
print('sum=', statis('sum', 1,2,3,4,5)) # TypeError


# 딕셔너리형 가변인자
def emp_func(name, age, **other):
    print(name)
    print(age)
    print("---")
    print(other)
    print(other['addr'], other['height'], other.get('weight'))

    print("---")
    for k in other.keys(): # 
        print(k, '=>',other[k], other.get(k))



emp_func('홍길돟',15, addr='서울시', height=175, weight=70)



    

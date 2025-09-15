#  일급함수와 함수 클로저

# 중첩 함수
# def 외부함수(인수):
#     실행문
#     ...
#     def 중첩함수(인수):
#         실행문
#         ...
#         return 값
#     return  내부 함수

# 1. 일급 함수
def a(): # outer
    print('a()함수 실행중...')

    def b(): # inner 함수 선언
        print('a()함수 안에 있는  b()함수')

    return b # a()함수 끝내고 b함수 자체를 반환

rs1 = a() # 외부 함수 호출
rs1() # 내부 함수 호출

# 함수 클로저: 외부함수가 종료되어도 내부 함수에서 선언된 변수가 
#  메모리에 소멸되지 않은 상태로 내부함수를 활용

data = list(range(1, 101))

def out_func(data): # outer function
    dataSet = data 

    # inner function
    def tot():
        tot_val = sum(dataSet)
        return tot_val # 합계 반환

    def avg(tot_val):
        avg_val = tot_val / len(dataSet)
        return avg_val #평균 반환
    
    return tot, avg # tot(), avg()함수를 반환

tot, avg = out_func(data) # out_func() 호출 수행하고 tot, avg에 함수를 반환(이미 객체가 만들어진 상태)

print('tot=', tot()) #총합 결과 값
print('avg=', avg(tot())) # 평균 결과 값





#함수: 내장함수, 사용자 정의함수
# : 특정 기능을 수행하는 독립된 단위 프로그램

#  builtins모듈에서 제공하는 함수 =>  import 없이 바로 사용

# builtins함수
dataset = list(range(1,6))
print(dataset)
print('len=', len(dataset))
print('sum=', sum(dataset))
print('max=', max(dataset))
print('min=', min(dataset))
print('avg=', sum(dataset)/len(dataset))


# import함수
# import statistics #  1. import 모듈명
from statistics import mean, median # 2. from 모듈명 import 함수명

# 1. 방식
# print('평균=', statistics.mean(dataset))# 평균
# print('중위수=', statistics.median(dataset)) # 중위수

# 2. 방식
print('평균=',  mean(dataset))# 평균
print('중위수=', median(dataset)) # 중위수

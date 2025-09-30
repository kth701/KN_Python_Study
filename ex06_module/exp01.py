# 예외 처리
# try:
#     pass
# except 예외처리 클래스 as 객체:
#     pass
# finally:
#     항상 실행 코드

print('프로그램 시작!!!')
x = [10,20,25.2,'num', 14,51]

for i in x:
    try:
        print(i)

        y = i**2
        print('y=', y)
    except:
        print('숫자가 아닌 데이터: ',i)

print('프로그램 종료')

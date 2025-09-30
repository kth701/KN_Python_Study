# 유형별 예외처리
print('유형별 예외처리')

try:
    div = 1000 / 2.53
    print('div= %5.2f' %(div))

    div = 1000 / 0  # 1차: 산술적 예외처리 발생
    f = open('c:\\test.txt') # 2차:  파일 열기 실패 예외 처리 발생
    num = int(input('숫자입력:')) # 3차 : 기타 예외처리

except ZeroDivisionError as e:
    print('오류 정보: ', e)
except FileExistsError as e:
    print('오류 정보: ', e)
except Exception as e:
    print('오류 정보: ', e)
finally:
    print('finally 영역 - 항상 실행되는 영역')
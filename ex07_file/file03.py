#파일 처리
# 텍스트 파일 : open(file, mode, encoding)

import os
print('현재 경로:'+os.getcwd()) #프로젝트 폴더위치-> 기본위치

#예외처리
try:
    # 파일 열기 => with open() ~ => auto close 기능 수행
    with open('ex07_file/test.txt', mode='r',encoding='utf-8') as ftest1:
    
        print('----')
        print(ftest1.read()) # 파일 전체 읽기

    # 파일 쓰기
    with open('ex07_file/test2.txt',mode='w',  encoding='utf-8') as ftest2:
        ftest2.write('my first text.....')

except Exception as e:
    print('Error: ', e)
finally:
    pass



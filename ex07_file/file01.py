#파일 처리
# 텍스트 파일 : open(file, mode, encoding)

import os
print('현재 경로:'+os.getcwd()) #프로젝트 폴더위치-> 기본위치

#예외처리
try:
    # 파일 열기
    ftest1 = open('ex07_file/test.txt', mode='r',encoding='utf-8')
    
    print('----')
    print(ftest1.read()) # 파일 전체 읽기

    # 파일 쓰기
    ftest2 = open('ex07_file/test2.txt',mode='w',  encoding='utf-8')
    ftest2.write('my first text.....')

except Exception as e:
    print('Error: ', e)
finally:
    ftest1.close()
    ftest2.close()



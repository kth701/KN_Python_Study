# os 모듈

import os

# 현재 작업 디렉토리 확인
print()
print("=> current path: ", os.getcwd())

# 작업 디렉토리 변경
os.chdir('ex08_filesystem')
print("=> change path: ", os.getcwd())

# 디렉토리 생성
# os.mkdir('test')
result_dir = os.listdir('.') # 현재 디렉토리 목록 확인
print(result_dir)

# os.chdir('test') # 디렉토리 변경(이동)
# print(os.getcwd())

os.rmdir('test')




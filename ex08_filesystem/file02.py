# 여러개의 디렉토리 처리 하기

import os

# 현재 작업 디렉토리 확인
print()
print("=> current path: ", os.getcwd())

# 작업 디렉토리 변경
os.chdir('ex08_filesystem')
print("=> change path: ", os.getcwd())

# os.mkdir('test/data') # error


# 디렉토리 유무 판단
# print(os.path.exists('test/data'))
path_boolean = os.path.exists('test/data')
if not path_boolean: # 디렉토리가 없으면 생성
    # 여러 개의 디렉토리 생성
    os.makedirs('test/data')
    # os.makedirs('test/data2')


os.chdir('test/data')
result_dir = os.listdir('.') # 현재 디렉토리 목록 확인-> List
print(result_dir)

print("---")
for cur_dir in result_dir:
    if os.path.isdir(cur_dir):
        print("<DIR>   :[{}]".format(cur_dir))
    else:
        print("파일:",cur_dir)


# 여러 개의 디렉토리 삭제
# os.removedirs('test/data')
# os.removedirs('test/data2')

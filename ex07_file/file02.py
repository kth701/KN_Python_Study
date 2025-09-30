# 텍스트 자료 읽기: 
# read() -> 전체 텍스트 한번에 읽기 -> 문자열 자료형을 반환
# readlines() -> 줄단위로 읽기 -> 리스트형으로 반환
# readline() -> 한 줄 단위 -> 문자열 자료형 반환



try:
    # 1. read()
    ftest1 = open('ex07_file/test.txt', mode='r', encoding='utf-8')
    
    # full_text = ftest1.read()
    
    # print("--- read() ")
    # print(full_text)
    # print("-"*5)
    # print(type(full_text))

    # from re import  sub 
    # # 2. readlines()
    # lines = ftest1.readlines()

    # print("--- read() ")
    # print(lines)
    # print("-"*5)
    # print(type(lines))
    # print('문단수: ',len(lines))

    # for txt in lines:
    #     print(sub('\n','', txt)) # '\n'제거한 후 출력

    # print("--------")

    
    # 3. readline()
    line = ftest1.readline()
    print(line)
    print(type(line))

except Exception as e:
    print('error=> ', e)
finally:
    ftest1.close()
# 획득자(getter), 지정자(setter)...
# 함수내의 자료를 외부로 획득하거나 자료를 수정한 역할

# def 외부함수():
#     변수명 = 값
#     def 내부함수():
#         nonlocal 변수명


# 중첩 함수
def main_func(num):
    num_val = num # 자료 생성

    def getter(): # 획득자 함수=> 함수내에서 생성한 자료를 외부로 반환
        return num_val
    
    def setter(value): # 지정자 함수 => 함수내부에서 생성한 자료를 외부에서 수정하는 함수
        nonlocal num_val
        num_val = value
    
    return getter, setter # 함수 클로저 반환

# 외부 함수 호출
getter, setter = main_func(100)
print('num=', getter())

setter(200)
print('num=', getter())
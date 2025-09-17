# 함수 장식자 => @함수명

# @함수 장식자
# def  함수명():
#     실행문

 # 래퍼 함수
def wrap(func):

    def decorated():
        print(' 방가워요!!!')

        func() # 함수호출 실행

        print(' 잘가요!!!')
    return decorated

@wrap
def hello():
    print('Hi~~~~', '홍길동')

hello() # 함수 호출

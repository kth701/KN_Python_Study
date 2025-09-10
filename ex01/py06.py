# 표준 입력(키보드)출력(콘솔) 장치

# value인수
print("value=", 10+20)
# sep인수 : 값과 값을 특수문자로 구분
print("010","1234","5678",sep="-")
# end인수
print("value=", 10, end=", ")
print("value=", 20)

# format과 양식 문자(%d, %o,%x, %f, %s, %c)
# format()=> 형식이 있는 출력 
print("원주율=", format(3.14159, "8.3f"))
print("원주율=", format(3.14159, "08.3f"))
print("금액=", format(10000, "10d"))
print("금액=", format(10000, "010d"))
print("금액=", format(10000, "10,d"))

#  양식 문자
name = "홍길동"
age = 25
price = 125.456

print("이름: %s, 나이: %d, data=%.2f" % (name, age, price))
print("이름: {}, 나이: {}, data={}".format(name, age, price))
print(f"이름: {name}, 나이: {age}, data={price:.2f}")

# uid = input("id input: ")
# query = f"select * from member where uid = {uid}"
# print(query)

print("-"*5)
#  문자열 유형
oneLine = "this is one line string"
print(oneLine)
print(type(oneLine))

multiLine = """\
안녕하세요
홍길동입니다.
만나서 반갑습니다.\
"""

print(multiLine)
print(type(multiLine))



# 슬라이싱(slicing)
oneLine = "this is one line string"
print(oneLine, ", len=", len(oneLine))

print("--- 슬라이싱")
print(oneLine[0:4]) # this => [startIndex, endIndex -1]
print(oneLine[5:7]) # is
print(oneLine[8:10]) # on

print("-"*5) 
print(oneLine[:4]) # [:n] => 첫번째 부터 n-1번째 까지
print(oneLine[:]) # 전체
print(oneLine[::2]) # 2씩 증가 [시작:끝:증가]

# 우측기준
txt_slice = "0123456789"
print(txt_slice[-6:-1]) # 마지막 index은 포함되지 않음:  45678 
print(txt_slice[-6:]) # 456789

# 부분 문자열 생성
temp = txt_slice[-5:]
print(temp) # 56789

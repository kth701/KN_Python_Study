# 다중 for

# 구구단
# for i in range(2, 9+1):
#     print("--- {}단 ---".format(i))

#     for j in range(1, 9+1):
#         print("{}*{} = {}". format(i, j, i*j))

str = """나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 19세 입니다."""

print(str)

sents = [] # 문장 저장
words = [] # 단어 저장

# 문단 -> 문장
print(str.split("\n"))

for sen  in str.split("\n"): # 줄단위 잘라서 리스트 구조 반환
    sents.append(sen) # 문장 저장

    # 문장 -> 단어
    for word in sen.split():
        words.append(word) # 단어

print("문장: ", sents)
print("문장수: " , len(sents))

print("단어: ", words)
print("단어수: " , len(words))

# 리스트(list), 튜플(tuple), 셋(set), 딕셔너리(dict)
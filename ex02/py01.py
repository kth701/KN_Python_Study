# 제어문
# if 조건식:
# [들여쓰기] 처리할 문장

# num1 = 10
# if num1 > 10:
#     print('num1=', num1)
#     print('조건이 참인 경우 처리되는 문장')

# print("제어문 벗어난 영역")

# num1 = int(input("정수: "))

# 1. 단순 if 
# if num1 % 2 == 0:
#     print("{}는 짝수입니다.".format(num1))

# 2. if else 
# if num1 % 2 == 0:
#     print(num1)
#     print("짝수")
# else:
#     print(num1)
#     print("홀수")

# print("다음 문장")

# 3. elif 
score = int(input("점수:"))
# if score >=90 and score<=100:
#     print("A")
# elif score >=80 and score<90:
#     print("B")
# else:
#     print("F")

# 비교연산 다른 형시 표현
# if 90 <= score <=100:
#     print("A")
# elif 80 <= score <90:
#     print("B")
# else:
#     print("F")  

# if score >= 60:
#     print("합격")
# else:
#     print("불합격")

result_score = "합격" if score >=60 else "불합격"
print(f"합격여부 결과=>{result_score}")










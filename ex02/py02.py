# 반복문 : for(반복횟수 명확할때  주로 사용) , while(참인동안 반복)

# cnt = tot = 0
# while cnt < 5:
#     cnt += 1
#     tot += cnt # +1, +2, +3, +4,...
#     print(cnt,tot)

# print("-"*5, "무한 반복")
# while True:
#     print("무한 반복 처리 중")

# while False:
#     print("한번도 수행 할 수가 없음")

# print("-"*5)

# num1 = 0
# while num1 < 5:
#     pass # 나중에 작성할 영역을 표시(에러 발생하지 않음)


# 무한 반복 사용예)

# while True:
#     num = int (input("숫자:"))
#     if num == 0:
#         break # 강제로 제어문 빠져나오기

#     if num % 5 == 0: # 5의배수는 출력 안됨
#         continue

#     print(f"입력한 숫자는 {num}")

# 1-100 사이의 3의 배수 합과 원소 추출하기
cnt1 = tot1 = 0
dataset = [] # 비어 있는 리스트 객체 선언=> 3의 배수를 보관

while cnt1 < 100:
    cnt1 += 1 # 1, 2, 3,.... ,100

     # 3의배수이면 => 저장, 누적
    if cnt1 % 3 == 0:
         # +3, +6, +9,...
         tot1 += cnt1 
         # 3의 배수 원소추가
         dataset.append(cnt1) 

print("-"*5, "결과 값")
print(f"1-100까지의 3의 배수의 합은 {tot1}")
print(dataset)



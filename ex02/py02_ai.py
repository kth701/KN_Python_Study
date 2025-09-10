# 1부터 100까지의 숫자 중에서 3의 배수를 찾고, 그 합을 계산합니다.
# while 루프와 list를 사용합니다.

# 변수 초기화
i = 1  # 1부터 시작할 카운터 변수
sum_of_multiples = 0  # 3의 배수 합계를 저장할 변수
multiples_of_3 = []  # 3의 배수를 저장할 리스트

# while 루프를 사용하여 1부터 100까지 반복
while i <= 100:
    # 현재 숫자가 3의 배수인지 확인 (3으로 나누었을 때 나머지가 0인지)
    if i % 3 == 0:
        # 3의 배수이면 리스트에 추가
        multiples_of_3.append(i)
        # 합계에 더하기
        sum_of_multiples += i
    
    # 다음 숫자로 넘어가기 위해 카운터 1 증가
    i += 1

# 결과 출력
print("1부터 100 사이의 3의 배수 리스트:")
print(multiples_of_3)

print(f"\n1부터 100 사이의 3의 배수의 합: {sum_of_multiples}")
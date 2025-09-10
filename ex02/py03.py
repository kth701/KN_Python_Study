# 난수 발생: random
import random

names = ["홍길동","홍길순","이순신","강감찬","김유신","유관순","안중근"]
print(names[0], names[1], names[2])

count = 0
while count < 5:
    count += 1

    # print("-"*15)
    # r = random.random() # 0 < r < 1
    # print('r=', r)

    # r2 = random.randint(100,120) # [a,b] 범위에서 난수 정수 반환
    # print('r2=', r2)

    rnd = random.randint(0,6) # 0-6사이 무작위 발생
    print('rnd=',rnd, names[rnd]) # name[3],....



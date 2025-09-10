# 리스트 테스트
list1 = [100, 200,300]
list2 = ["홍길동","홍길순"]

list3 = list1 + list2
print(list3)

# list4 = list3 + 400 # 타입에러 발생
list4 = list3 + [400]
print(list4)

list5 = [ 1, 2, 3, [100,200], [True,False], ["홍길동","홍길순"]]
print(list5[0],list5[1],list5[2],list5[3],list5[4],list5[5])
print(list5[3][0],list5[3][1])








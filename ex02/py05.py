# range객체 생성
num1 = range(10) # range(start)
print(num1, type(num1))

num2 = range(1,10) # range(start, stop)
print(num2, type(num2))

for n1 in num1:
    print(n1, end=" ")

print("\n","-"*5)

for n2 in num2:
    print(n2, end=" ")

print("\n","-"*5)

for n3 in range( 1,10+1, 2):
    print(n3, end=" ")

print("\n","-"*5)

nums = [1,2,3,4,5,6,7,8,9,10]
for number in nums:
    if number%5 == 0:
        print(number, end = " ")

print("\n","-"*5)
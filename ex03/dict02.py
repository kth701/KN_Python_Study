# 요소 검사
person = {'name':'홍길동', 'age':35, 'address':'서울시'}
print( 'age' in person) # True
print( 'gender' in person) # False

print("person: {}".format(person))
print("key나열: {}".format(person.keys()))
print("value나열: {}".format(person.values()))
print(f"key와 value 나열{person.items()}")

print("-- keys()")
for key in person.keys():
    print(key, end=' ')
print()

print("-- values()")
for value in person.values():
    print(value, end=' ')
print()

print("-- items()")
for item in person.items():
    print(item, end=' ')
print()
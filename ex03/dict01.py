# dict(딕트): key,value 쌍으로 저장하는 구조
# 중괄호=> {'키':'값',.....} 형식

# 생성1: 생성자 이용
dic = dict(key1=100, key2=200, key3=300)
print(dic, type(dic))

# 생성2: 
person = {'name':'홍길동', 'age':35, 'address':'서울시'}
print(person)

print(person['name'], person.get('name'))
print(person['age'])
print(person['address'])

person['name']='동순이'
print(person)

person['gender']='남자' # 없는 키에 값을 설정시 => 추가
print(person)

del person['gender'] # 삭제
print(person)




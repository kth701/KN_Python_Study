# import 모듈 내장 클래스
# import 모듈, from 모듈,.. import fn1, fn2,..



# import datetime
# today = datetime.date(2025,9,24)


from datetime import date, time
# help(date)
# print("-"*20)

today = date(2025,9,24)
print(today)

print(today.year)
print(today.month)
print(today.day)

w = today.weekday()
print('요일 정보: ',w) # 0:월,...6:일

currTime = time(22,4,10)
print(currTime)
print(currTime.hour,currTime.minute, currTime.second)

isTime = currTime.isoformat()
print(isTime)
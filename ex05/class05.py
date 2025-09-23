# 캡슐화
class Account:
    # 은닉 멤버변수
    # __변수명 => private 변수명 동일 구조
    __balance = 0 # 잔액
    __accName = None #예금주
    __accNo = None # 계좌 번호

    # 생성자
    def __init__(self, bal, name, no):# 잔액, 예금주, 계좌번호
        self.__balance = bal # 잔액 초기화
        self.__accName = name # 예금주
        self.__accNo = no # 계좌번호

    # 계좌 정보 확인
    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo
    
    # 입금하기: Setter
    def deposit(self, money):
        if money < 0:
            print('금액 확인')
            return # 함수 종료
        
        self.__balance += money

    
    # 출금하기: Getter
    def withdraw(self, money):
        if self.__balance < money:
            print('잔액 부족')
            return 
        self.__balance -= money


# object 생성
acc = Account(1000, '홍길동', '123-123-1111-01')

# Getter
# acc.__balance # 오류 : 접근 에러 private(은닉)

# bal = acc.getBalance()
print('계좌 정보:',acc.getBalance())

# Setter호출
acc.deposit(-100)
acc.deposit(1000)
print('계좌 정보:',acc.getBalance())

acc.withdraw(100)
print('계좌 정보:',acc.getBalance())


 


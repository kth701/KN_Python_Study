# 상속
# 부모 클래스
class Super:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 멤버 메서드
    def display(self):
        print('name: %s, age : %d'%(self.name, self.age))

# 부모 클래스 객체 생성
sup = Super('부모', 55)
sup.display()

# 자식 클래스
class Sub(Super): # 자식클래스(상속받을 부모클래스)
    genter = None   # 자식에서 정의한 멤버변수

    def __init__(self, name, age, gender):
        # name,age 부모클래스자원 이기때문에 부모생성자로 통해 초기화 해야한다.
        super().__init__(name, age)
        
        # self.name = name
        # self.age = age
        self.genter = gender

    def display(self):
        print('name: %s, age: %d, gender: %s'%(self.name, self.age, self.genter))

sub = Sub('자식객체', 25, '남자')
sub.display()

sup.display()

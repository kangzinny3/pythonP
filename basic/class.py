class Cookie:    # 첫 글자는 대문자로 하는 것이 관례
    pass         # 아무것도 수행하지 않는 문법으로 임시로 코드를 작성할 때 주로 사용

a = Cookie()     # a, b는 객체 / 객체 a는 Cookie의 인스턴스
b = Cookie()

print(id(a), id(b))
print(type(a), type(b))

class FourCal:
    first = 0     
    second = 0
    def setdata(self, first, second):   # 메서드(함수)의 매개변수
        self.first = first              # 메서드의 수행문
        self.second = second            # 메서드의 수행문

a = FourCal()
a.setdata(4, 2)  # 함수를 정의할 때는 3개의 매개변수를 썼는데 실제로는 2개 값만 전달
                 # 첫 번째 매개변수 self는 관례적으로 사용하는 것 / self가 아니어도 됨
                 # 객체를 호출할 때 호출한 객체 자신이 전달됨 / a-self, 4-first, 2-second
print((a.first), (a.second))     # 클래스에서 정의한 변수에 접근할때는 객체.메서드 형식으로 호출

# 사칙연산 클래스 만들기
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()  
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)
print(a.add(), b.sub())

# 생성자 : 객체를 생성하는 시점에 만들어지는 함수 / __init__ 을 사용하여 생성
class FourCal:
    def __init__(self, first=4, second=2):
        self.first = first
        self.second = second   
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()       # first, second의 초깃값이 없다면 a=FourCal(4, 2)처럼 
print(a.add())      # 생성자 앞에 first, second의 초깃값을 설정

# 클래스의 상속
class MoreFourCal(FourCal):    # FourCal 클래스를 상속받음
    pass
a = MoreFourCal()
print(a.add())

# 메서드 오버라이딩 : 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것
class SafeFourCal(FourCal):
    def div(self):     # 부모 클래스(FourCal)의 div함수를 가져옴
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div())

# 클래스 변수
class Family:
    lastname = '강'

print(Family.lastname)     # 클래스이름.클래스변수
a = Family()
b = Family()
print(a.lastname, b.lastname)

Family.lastname = '김'
print(a.lastname, b.lastname)    # 클래스 변수는 클래스로 만든 모든 객체에 공유됨
                                 # id 값을 출력해보면 같은 메모리
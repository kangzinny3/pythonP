class Cookie:    # 첫 글자는 대문자로 하는 것이 관례
    pass         # 아무것도 수행하지 않는 문법으로 임시로 코드를 작성할 때 주로 사용

a = Cookie()     # a, b는 객체 / 객체 a는 Cookie의 인스턴스
b = Cookie()

print(id(a), id(b))
print(type(a), type(b))

class FourCal:
    first = 0     
    second = 0
    def setdata(self, first, second):  
        self.first = first     
        self.second = second

a = FourCal()
a.setdata(4, 2)  # 함수를 정의할 때는 3개의 매개변수를 썼는데 실제로는 2개 값만 전달
                 # 첫 번째 매개변수 self는 관례적으로 사용하는 것 / self가 아니어도 됨
                 # 객체를 호출할 때 호출한 객체 자신이 전달됨 / a-self, 4-first, 2-second
print((a.first), (a.second))

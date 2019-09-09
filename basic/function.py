def add(a, b):
    return a + b

a = 4           # print(add(a = 4, b = 6))
b = 6
c = add(a, b)    # print(add(a, b))
print(c)

# 입력값이 여러 개일 때 -> 매개변수 앞에 *를 붙여서 변수 선언
def add_many(*args):    # 값을 튜플로 받음
    result = 0
    for i in args:
        result += i
        print(i)
    return result
sum = add_many(1, 2, 3, 4, 5, 6)
print(sum)

# 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print('나의 이름은 {}'.format(name))
    print('나이는 %d살 입니다.' % old)
    if man:
        print('남자')
    else:
        print('여자')
say_myself('지은', 26, man=False)  # man값을 설정하지않고 ('지은', 26)만 하면 '남자'로 출력
                                   # man=False를 False만 입력해도 상관 없음

# lambda 함수
   # lambda 매개변수1, 매개변수2 : 표현식

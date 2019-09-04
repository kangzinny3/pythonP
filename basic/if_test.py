pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")

score = int(input("점수를 입력해주세요: "))
message = "success" if score >= 60 else "failure"

# 주민등록번호를 입력받고 성별 출력하기
id = input("주민등록번호를 입력해주세요: ")
if id[7] == '1' or id[7] == '3':
    print("남자")
elif id[7] == '2' or id[7] == '4':
    print("여자")

# while문 사용하기
coffee = {'아메리카노':2500, '카페라떼':3000, '카푸치노':3500}
order = 0
while order != '3':
    order = input('주문번호를 입력해주세요: ')
    if order == '1':
        menu = input('메뉴를 입력하세요: ')
        price = input('가격을 입력하세요: ')
        print("메뉴 이름은 {}이고, 가격은 {}원입니다.".format(menu, price))
    elif order == '2':
        for i in coffee:
            print(i, end=' ')
            print()
        menuname = input("선택: ")
        for j, k in coffee.items():
            if j == menuname:
                print(k)
    elif order == '3':
        pass
    else:
        print("주문번호를 다시 입력하세요")

# for문을 이용해 짝수의 합 출력하기
add = 0
n = int(input('숫자를 입력해주세요: '))
for i in range(1, n+1):
    if i % 2 == 0:
        add += i
    else:
        pass
print("1부터 {}까지 짝수의 합은 {}입니다.".format(n, add))

# for와 range를 이용해 구구단 출력하기
for i in range (2, 10):
    for j in range(1,10):
        k = i * j
        print(i, 'x', j, '=', k, end='  ')
    print()

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result)

a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

# 짝수만
a = [1, 2, 3, 4]
result = [num * 3 in a if num % 2 == 0]
print(result)

# 덧셈문제 맞추기
import random
count = 0
for i in range(0,5):
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    print("%d + %d =" % (a, b))
    c = int(input())
    if a + b == c:
        print('정답입니다.')
        count += 1
    else:
        print('틀렸습니다.')
print("%d개 맞았습니다." % count)

# 사칙연산 맞추기
import random
count = 0
oper = ['+', '-', '*', '/']
for i in range(0,5):
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    op = random.choice(oper)
    quiz = str(a) + op + str(b)
    print(quiz)
    c = int(input())
    if int(eval(quiz)) == c:
        print('정답입니다.')
        count += 1
    else:
        print('틀렸습니다.')
print("%d개 맞았습니다." % count) 

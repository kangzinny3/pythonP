import time
print(time.asctime(time.localtime(time.time())))
ww = ('일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일')

print(time.strftime('%Y %m %d %w', time.localtime(time.time())))
s = time.strftime('%Y %m %d %w', time.localtime(time.time()))
print(ww[int(s[-1])])

# for i in range(1, 11):
#     print(i, '초', sep='')
#     time.sleep(1)

# 시간 맞추기 게임
input('엔터를 누르고 20초를 셉니다.')
start = time.time()
input('20초 후에 다시 엔터를 누릅니다.')
end = time.time()
et = end - start
print('실제 시간 : {:.0f}초'.format(et))
print('차이 : {:.0f}초'.format(abs(et - 20)))  # abs = 절대값 구하는 함수

# 로또 번호 생성하기 - 1
import random

for i in range(5):
    lotto = [0, 0, 0, 0, 0, 0] # 0으로 초기값을 설정해서 중복 여부 파악
    for j in range(6):
        num = 0  # num => 뽑은 숫자
        while(num in lotto):   # 중복되지 않게 숫자를 뽑도록 
            num = random.randint(1, 45)
        lotto[j] = num
    print('로또 : ', sorted(lotto))

# 로또 번호 생성하기 - 2
for i in range(1, 6):
    print('로또 : ', sorted(random.sample(range(1, 45), 6)))

# dict 정렬하기
score = [26, 21, 14, 24, 8]
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
score.sort()   # sort - 리스트에서 제공하는 함수 / 정렬할 때 사용
print(score)

print(sorted(names))   # key값을 정렬해서 새로운 리스트를 리턴
print(names)   # 딕셔너리가 그대로 출력됨

# value값을 기준으로 정렬
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
def f1(x):
   return x[1]   # x의 인덱스 0이면 key값, 인덱스 1이면 value값
res = sorted(names.items(), key = f1)   # reverse = True를 추가하면 큰 값부터 정렬
print(res)

# 야구 게임 - 1
# import random

# num = random.sample(range(1, 10), 3)
# game_count = 0
# st_count = 0
# bl_count = 0

# while st_count < 3:
#     n = input('숫자를 입력해주세요: ')
#     for i in range(3):
#         for j in range(3):
#             if (n[i] == str(num[j]) and i == j):
#                 st_count += 1
#             elif (n[i] == str(num[j]) and i != j):
#                 bl_count += 1
#     game_count += 1
#     print(st_count, '스트라이크', bl_count, '볼')   
# print(game_count, '번만에 정답!', sep='')

# 야구 게임 - 2
com = random.sample(range(1, 10), 3)
print(com)
strike = 0
check = 0
print('시작')
start = time.time()
while strike != 3:
    strike = 0
    ball = 0
    guess = list(input('3자리 숫자를 입력하세요: '))
    print(guess)
    for i in guess:
        for j in com:
            if int(i) == j:
                if guess.index(i) == com.index(j):
                    strike += 1
                else:
                    ball += 1
    check += 1
    print('스트라이크:%d, 볼:%d, 시도횟수:%d' % (strike, ball, check))
end = time.time()
print('정답! 걸린시간은 {:.0f}초 입니다.'.format(end - start))

# 타자 게임
import random, time

words = ['strawberry', 'dog', 'wendy', 'jieun', 'reo', 'yuchang']
n = 1
input('엔터를 누르면 게임을 시작합니다.')
start = time.time()
q = random.choice(words)

while n <= 5:
    print('{}번 문제'.format(n))
    print(q)
    x = input()
    if q == x:
        print('정답입니다.')
        n += 1
        q = random.choice(words)
    else:
        print('틀렸습니다.')
end = time.time()
print('걸린 시간은 {:.0f}초 입니다.'.format(end - start))
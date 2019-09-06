# 타자 게임

import random, time
words = ['strawberry', 'dog', 'wendy', 'jieun', 'reo', 'yuchang']
while True:
    print('1.문제 불러오기  2.타자게임  3.종료하기')
    menu = input('메뉴를 선택하세요\n')
    if menu == '1':
        f = open('./basic/word.txt', 'r', encoding='utf8')
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n', '')
        words += lines
        print(words)
        f.close()        
    elif menu == '2':
        n =1
        q = random.choice(words)
        input('엔터를 누르면 시작합니다.')
        start = time.time()
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
    elif menu == '3':
        print('종료합니다.')
        break

'''
# 두 번째 방법
if menu == '1':
    f = open('./basic/word.txt', 'r', encoding='utf8')
    line = 1
    while line:
        line = f.readline().replace('\n', '')
        if not(line == '')
            words.append(line)
    print(words)
    f.close()

# 왜 안될까
if menu == '1':
    f = open('./basic/word.txt', 'r', encoding='utf8')
    lines = f.readlines()
    for line in lines:
        line = line.rstrip('\n')      # line = line.replace('\n','')
        words.append(line)
        print(lines)
    f.close()
'''
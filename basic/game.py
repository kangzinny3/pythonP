# 타자 게임

import random, time, pickle

words = ['오렌지', '바나나', '강아지', '고양이', '토끼']

with open('./basic/rank.pkl', 'rb') as f:
    rank = pickle.load(f)

while True:
    print('''
        1.문제 불러오기 
        2.문제 추가하기 
        3.문제를 피클로 저장 
        4.피클 문제 읽기 
        5.타자게임 
        6.등수 확인하기
        7.종료하기
        ''')
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
        quiz = 1
        while quiz:
            quiz = input('추가할 단어를 입력해주세요(0을 누르면 종료됩니다).: ')
            if quiz == '0':
                print('입력을 종료합니다.')
                break
            words.append(quiz)
        print(words)
    elif menu == '3':
        with open('./basic/pickle.pkl', 'wb') as f:
            pickle.dump(words, f)
    elif menu == '4':
        with open('./basic/pickle.pkl', 'rb') as f:
            words = pickle.load(f)
        print(words)
    elif menu == '5':
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
        name = input('이름을 입력해주세요.: ')
        rank[name] = end - start
        print(rank)
    elif menu == '6':
        ranklist = sorted(rank.items(), key = (lambda x : x[1]))

        cnt =1
        for k, v in ranklist:
            print('{}등: {}, 시간: {:.2}'.format(cnt, k, v))
            cnt += 1
    elif menu == '7':
        with open('./basic/rank.pkl', 'wb') as f:
            pickle.dump(rank, f)        
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
import random, time, pickle

words = ['오렌지', '바나나', '강아지', '고양이', '토끼']
rank = {} 

# 문제 불러오기
def rankLoad(r):
    rank = r
    with open('./rank.pkl', 'rb') as f:
        rank = pickle.load(f)   # 지역변수
    return rank
rankLoad(rank)


# 문제 txt 저장하기
def wordLoadTxt(w):
    words = w
    f = open('./word.txt', 'r', encoding='utf8')   
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
    words += lines
    print(words)
    f.close()


# 문제 추가하기 
def wordSaveTxt(w):
    words = w
    f = open('./word.txt', 'r', encoding='utf8')
    for i in words:
        data = ''
        data += i + '\n'
        f.write(data)
    f.close()


# 문제 추가하기
def wordAppend(w):
    words = w
    quiz = 1
    while quiz:
        quiz = input('추가할 단어를 입력해주세요(0을 누르면 종료됩니다).: ')
        if quiz == '0':
            print('입력을 종료합니다.')
            break
        words.append(quiz)
    print(words)


# 문제를 피클로 저장
def wordSavePik(w):
    words = w
    with open('./pickle.pkl', 'wb') as f:
        pickle.dump(words, f)


# 피클 문제 읽기
def wordLoadPik(w):
    words = w
    with open('./pickle.pkl', 'rb') as f:
        words = pickle.load(f)
    print(words)


# 타자게임 
def game(r, w):
    rank = r
    words = w
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


# 등수 확인하기
def rankList(r):
    rank = r
    ranklist = sorted(rank.items(), key = (lambda x : x[1]))

    cnt =1
    for k, v in ranklist:
        print('{}등: {}, 시간: {:.2}'.format(cnt, k, v))
        cnt += 1


# 종료하기
def endGame(r):
    rank = r
    with open('./rank.pkl', 'wb') as f:
        pickle.dump(rank, f)        
    print('종료합니다.')
    
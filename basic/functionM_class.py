import random,time, pickle, os, sys


class TypingGame:

    words = ['오렌지', '바나나', '강아지', '고양이', '토끼']
    rank = {} 

    def __init__(self):
        self.rankLoad()
        while True:
            self.exe(self.menuDisplay())

    def rankLoad(self):
        if os.path.exists('./rank.pik'):
            f = open('./rank.pik', 'rb')
            self.rank = pickle.load(f)

# 문제 불러오기
    def wordLoadTxt(self):
        f = open('./word.txt', 'r', encoding='utf8')   
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n', '')
        self.words += lines
        print(self.words)
        f.close()

# 문제 txt 저장하기
    def wordSaveTxt(self):
        f = open('./word.txt', 'r', encoding='utf8')
        for i in self.words:
            data = ''
            data += i + '\n'
            f.write(data)
        f.close()

# 문제 추가하기
    def wordAppend(self):
        quiz = 1
        while quiz:
            quiz = input('추가할 단어를 입력해주세요(0을 누르면 종료됩니다).: ')
            if quiz == '0':
                print('입력을 종료합니다.')
                break
            self.words.append(quiz)
        print(self.words)

# 문제를 피클로 저장
    def wordSavePik(self):
        with open('./pickle.pkl', 'wb') as f:
            pickle.dump(self.words, f)

# 피클 문제 읽기
    def wordLoadPik(self):
        with open('./pickle.pkl', 'rb') as f:
            self.words = pickle.load(f)
        print(self.words)

# 타자게임 
    def game(self):
        n =1
        q = random.choice(self.words)
        input('엔터를 누르면 시작합니다.')
        start = time.time()
        while n <= 5:
            print('{}번 문제'.format(n))
            print(q)
            x = input()
            if q == x:
                print('정답입니다.')
                n += 1
                q = random.choice(self.words)
            else:
                print('틀렸습니다.')
        end = time.time()
        print('걸린 시간은 {:.0f}초 입니다.'.format(end - start))
        name = input('이름을 입력해주세요.: ')
        self.rank[name] = end - start
        print(self.rank)

# 등수 확인하기
    def rankList(self):
        ranklist = sorted(self.rank.items(), key = (lambda x : x[1]))

        cnt =1
        for k, v in ranklist:
            print('{}등: {}, 시간: {:.2}'.format(cnt, k, v))
            cnt += 1

# 종료하기
    def endGame(self):
        with open('./rank.pkl', 'wb') as f:
            pickle.dump(self.rank, f)        
        print('종료합니다.')

# 메뉴 디스플레이
    def menuDisplay(self):
        print('''
            1.문제 불러오기 
            2.문제 txt 저장하기
            3.문제 추가하기 
            4.문제를 피클로 저장 
            5.피클 문제 읽기 
            6.타자게임 
            7.등수 확인하기
            8.종료하기
            ''')
        menu = input('메뉴를 선택하세요\n')   
        return menu

# 메뉴 실행
    def exe(self, menu):
        if menu == '1':
            self.wordLoadTxt()
        elif menu == '2':
            self.wordSaveTxt()
        elif menu == '3':
            self.wordAppend()
        elif menu == '4':
            self.wordSavePik()
        elif menu == '5':
            self.wordLoadPik()
        elif menu == '6':
            self.game()
        elif menu == '7':
            self.rankList()
        elif menu == '8':
            self.endGame()


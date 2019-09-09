# 타자 게임

import functionM as fm

words = ['오렌지', '바나나', '강아지', '고양이', '토끼']
rank = {}   # 전역변수

rank = fm.rankLoad(rank)
     
        
while True:
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
    if menu == '1':
        fm.wordLoadTxt(words)
    elif menu == '2':
        fm.wordSaveTxt(words)
    elif menu == '3':
        fm.wordAppend(words)
    elif menu == '4':
        fm.wordSavePik(words)
    elif menu == '5':
        fm.wordLoadPik(words)
    elif menu == '6':
        fm.game(rank, words)
    elif menu == '7':
        fm.rankList(rank)
    elif menu == '8':
        fm.endGame(rank)


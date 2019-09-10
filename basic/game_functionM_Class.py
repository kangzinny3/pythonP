# 타자 게임

import functionM_Class as fmc


a = fmc.TypingGame()
     
        
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
        a.wordLoadTxt()
    elif menu == '2':
        a.wordSaveTxt()
    elif menu == '3':
        a.wordAppend()
    elif menu == '4':
        a.wordSavePik()
    elif menu == '5':
        a.wordLoadPik()
    elif menu == '6':
        a.game()
    elif menu == '7':
        a.rankList()
    elif menu == '8':
        a.endGame()


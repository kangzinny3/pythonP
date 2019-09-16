import mariadbFunc as f

f.conn_db()

while True:
    print('''
        1. 테이블 생성
        2. 데이터 입력
        3. 데이터 출력
        4. 데이터 수정
        5. 데이터 삭제
        6. 종료하기
        ''')
    menu = input("메뉴를 선택하세요.: ")
    if menu == '1':
        f.create_table()
    elif menu == '2':              # 에러가 발생하면 벌크 테이블 편집기 -> 문자 집합 변환
        title = input("책 제목: ")
        date = input("출판일: ")
        publisher = input("출판사: ")
        pages = int(input("페이지수: "))
        recommend = int(input("추천: "))
        item = (title, date, publisher, pages, recommend)
        f.insert_books(item)
    elif menu == '3':
        try:
            count = int(input("출력할 건수는? : "))
        except ValueError:
            count = 0
        f.all_books(count)
    elif menu == '4':
        pass
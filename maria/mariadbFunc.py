import pymysql

# 커넥션 함수
def conn_db():
    conn = pymysql.connect(host = 'localhost',
                            user = 'root',
                            password = 'qwer1234',
                            db = 'test')
    return conn

# 테이블 생성 함수
def create_table():
    conn = conn_db()
    c = conn.cursor()
    sql = '''
        create table if not exists books(
        title text,
        date text,
        publisher text,
        pages integer,
        recommend integer
        )'''
    c.execute(sql)
    conn.commit()
    conn.close()

# 데이터 입력 함수
def insert_books(item):
    conn = conn_db()
    c = conn.cursor()
    # # 데이터 입력방법1 
    # c.execute("insert into books values('Java','2019-05-20','길벗',500,10)")
    # # 데이터 입력방법2 
    # sql = 'insert into books values(%s,%s,%s,%s,%s)' 
    # c.execute(sql,('Python','2010-01-05','한빛',584,20)) 
    # # 데이터 입력방법3 
    sql = 'insert into books values(%s,%s,%s,%s,%s)' 
    c.execute(sql, item) 
    conn.commit() 
    conn.close()

# 데이터 출력 함수
def all_books(count = 0):
    conn = conn_db()
    c = conn.cursor()
    c.execute("select * from books")
    if count == 0:
        print('전체 데이터 출력하기')
        books = c.fetchall()
        print(books)
        # for book in books: 
        #     for i in book:
        #         print(book[i], end=" ") 
        #     print()
    else:
        books = c.fetchmany(count)
        print(books)
        # for book in books: 
        #     for i in book:
        #         print(book[i], end=" ") 
        #     print()    
    conn.close()    

# 데이터 수정 함수
def update_books():
    conn = conn_db
    c = conn.cursor()
    # title이 빅데이터인 recommend를 200으로 수정
    sql = '''update books
            set recommend = %s where title = %s'''
    c.execute(sql, 200, '빅데이터')
    conn.commit()
    conn.close()
    
# 데이터 삭제 함수
def delete_books():
    conn = conn_db
    c = conn.cursor()
    
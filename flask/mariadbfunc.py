import pymysql

def conn_db(): 
    conn = pymysql.connect(host='localhost', 
    user ='root', 
    password ='qwer1234', 
    db ='test' ) 
    # charset='utf8', 
    # cursorclass=pymysql.cursors.DictCursor
    return conn

#테이블 생성 함수 
def create_table(): 
    conn = conn_db() 
    cursor = conn.cursor() 
    # my_books테이블 생성(제목,출판일자,출판사,페이지수,추천여부) 
    cursor.execute('''
    create table if not exists books( 
        title text, 
        published_date text, 
        publisher text, 
        pages integer, 
        recommend integer 
        )''') 
    conn.commit() 
    conn.close()

# 데이터 입력 함수 
def insert_books(item): 
    conn = conn_db() 
    cursor = conn.cursor() 
    sql = 'insert into books values(%s,%s,%s,%s,%s)' 
    cursor.execute(sql,item) 
    conn.commit() 
    conn.close()

# 전체 데이터 출력 함수 
def all_books(count=0): 
    conn = conn_db() 
    cursor = conn.cursor() 
    cursor.execute("select * from books")
    if count == 0:
        print('[1] 전체 데이터 출력하기')
        books = cursor.fetchall() 
        print(books)
        for book in books: 
            print(book)
                
    else:
        books = cursor.fetchmany(count)
        print(books)
        for book in books: 
            print(book) 
    conn.close()
    return books

# 조건 지정
def where_book(where_v):
    conn = conn_db()
    cursor = conn.cursor()
    sql = 'select * from books where title=%s'   # title이 입력받은 문자(%S)와 같은지
    cursor.execute(sql, where_v)
    book = cursor.fetchone()
    print(book)
    conn.close()
    return book

# 삭제 함수
def delete(title):
    conn = conn_db()
    cursor = conn.cursor()
    sql = 'delete from books where title=%s'
    cursor.execute(sql, title)
    conn.commit()
    conn.close()

# 수정 함수
def update():
    conn = conn_db()
    cursor = conn.cursor()
    sql = 'update books set'

import sqlite3

'''
# 테이블 생성 함수
def create_table():           # 들어올 값이 있으면 ()안에 매개변수 선언
    conn = sqlite3.connect('my_books.db')
    c = conn.cursor()
    c.execute('''create table if not exists books( 
        title text,
        published_date text,
        pages integer,
        recommend integer
        )''')
                # my_books 테이블 생성(제목, 출판일자, 출판사, 페이지수, 추천여부)
    conn.commit()
    conn.close()
'''
# 커넥션 함수
def get_conn(file_info):
    conn = sqlite3.connect(file_info)   
    return conn
            # 커넥션이 필요하면 매개변수로 conn을 선언 ex. def create_table(conn):

def create_table(conn):
    c = conn.cursor()
    sql = '''
    create table if not exists books(
        title text,
        published_date text,
        pages integer,
        recommend integer
        )'''
    c.execute(sql)
    conn.commit()
    conn.close()

# 데이터 입력 함수


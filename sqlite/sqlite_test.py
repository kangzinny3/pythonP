import sqlite3

print(sqlite3.version)              # sqlite3 모듈 자체 버전
print(sqlite3.sqlite_version)       # sqlite 버전

# sqlite expert : http://www.sqliteexpert.com/download.html 에서 다운



conn = sqlite3.connect('D:/ai/pythonP/sqlite/example.db')    # 커넥션 객체를 받아야함 
cursor = conn.cursor()               # 커서 받아내기
cursor.execute('''CREATE TABLE if not exists stocks 
              (date text, trans text, symbol text, qty real, price real)''')     # 실행 -> 실행할 쿼리문을 ''' ''' (한 줄짜리 문자열이 아닐 때) 안에 넣어줌
              # CREATE TABLE : 테이블을 만듦 (관계형 db는 테이블 형태로 저장됨)
              # if not exists stocks : 테이블이 없으면 -> 처음에만 테이블을 만들고 그 다음부터는 만들지 않음
              # data text, trans text ... : data-컬럼 이름 /  text-텍스트 형태 / real-실수 형태 
              # 실행할 수 있는 쿼리문 : https://www.sqlite.org/lang.html        
              # 쿼리문이 너무 길면 sql = ''' ''' 식으로 따로 지정해서 실행하기도 함
sql = ("INSERT INTO stocks VALUES ('2019-09-11','BUY','RHAT',100,35.14)")    # 문자열은 작은 따옴표로 감싸줌
        # 원래 INTO stocks 사이에 컬럼 이름을 넣어줌 / 순서대로 넣을 때는 생략하기도 하지만, 넣어주는 것이 좋음
        # "INSERT INTO stocks (date text, trans text, symbol text, qty real, price real) VALUES ('2019-09-11','BUY','RHAT',100,35.14)"
        # date text-'2019-09-11' / trans text-'BUY' ... 순서로 매치
cursor.execute(sql)
conn.commit()     # 실행하는 내용이 변화가 있으면 commit해야 함
conn.close()

# sqlite expert에서 open database로 example.db 열기


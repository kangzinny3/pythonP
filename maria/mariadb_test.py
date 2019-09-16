import pymysql

conn = pymysql.connect(host = 'localhost',
                        user = 'root',
                        password = 'qwer1234',
                        db = 'test',
                        cursorclass = pymysql.cursors.DictCursor)  # DictCursor -> 딕셔너리로 출력 가능
c = conn.cursor()
# symbol  = input('심볼을 입력하세요.: ')
# sql = "select * from stocks where symbol='%s'" %symbol  # 문자열을 만들 때 -> sqlite3, pymysql에서 둘 다 가능
# c.execute(sql)

symbol  = input('심볼을 입력하세요.: ')
sql = 'select * from stocks where symbol=%s'    # symbol=? 하면 에러 발생
c.execute(sql, (symbol,))
print(c.fetchall())     # cf. fetchone, fetchmany

#데이터 여러개 추가하기
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
            ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
            ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (%s,%s,%s,%s,%s)', purchases)
conn.commit()
c.execute('select * from stocks order by price')
rows = c.fetchall()
for row in rows:
    print(row)
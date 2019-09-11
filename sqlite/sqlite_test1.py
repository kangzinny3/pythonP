import sqlite3

conn = sqlite3.connect('D:/ai/pythonP/sqlite/example.db')
c = conn.cursor()
'''
symbol = input('심볼을 입력하세요(ex: RHAT).: ')
sql = "SELECT * FROM stocks WHERE symbol = '%s'" % symbol     # 값이 문자열이므로 %s
# * : 전부 다 / 필드명을 명시해서 쓰는 것을 권함
c.execute(sql)
print(c.fetchone())
conn.close()
'''
'''
# 데이터 타입을 맞추지 않고, 자리만 맞춰주면 됨
symbol = input('심볼을 입력하세요(ex: RHAT).: ')
sql = 'SELECT * FROM stocks WHERE symbol=?' 
symbol = (symbol,)    # 튜플에서 한 개일 때 -> 콤마 필수!
c.execute(sql, symbol)
print(c.fetchone())
conn.close()
'''

# 데이터 여러개 처리하기 - 리스트로 묶기
# 하나의 데이터만 추가할때는 insert 사용
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00), 
            ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00), 
            ('2006-04-06', 'SELL', 'IBM', 500, 53.00), 
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
conn.commit()

c.execute('select * from stocks ORDER BY price')    # 정렬의 기본은 오름차순(Asc) - 내림차순으로 하려면 Desc
rows = c.fetchall()
for row in rows:
    print(row)

for row in c.execute('select * from stocks ORDER BY price'):
    print(row)

c.close()

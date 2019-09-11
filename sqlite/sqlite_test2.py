import sqlite3, csv

conn = sqlite3.connect('D:/ai/pythonP/sqlite/suppliers.db')
c = conn.cursor()
sql = '''
    create table if not exists suppliers(
        supplier_name varchar(20),       
        invoice_number varchar(20), 
        part_number varchar(20), 
        cost float, 
        purchase_date date
    )
    '''
                            # 필드명 varchar 길이는 20
c.execute(sql)

sql = 'delete from suppliers'        
c.execute(sql)
conn.commit()

# csv 파일에서 데이터를 읽어서 테이블에 insert 
# file_reader = csv.reader(open(input_file,'r', encoding='utf-8'), delimiter=',') 
input_file = 'D:/ai/pythonP/sqlite/input.csv'
file_reader = csv.reader(open(input_file,'r'))     #  delimiter : 구분자 / quotechar='"' : "로 싸져 있을 때

# 첫 라인을 읽음 / header : 첫 줄
header = next(file_reader, None)
print('header :', header)

# header 이후의 2번째 행부터 끝까지 읽어 들이며 insert (csv 데이터를 db에 넣음)
for row in file_reader:
    data = []
    for idx in range(len(header)):      # idx는 0~4가 입력됨
        data.append(row[idx])
    c.execute('insert into suppliers values(?,?,?,?,?)', data)
                    # 실행할 쿼리문이 긴 경우에는 sql변수를 따로 두고 c.execute(sql, data) 하면 됨
conn.commit()

output=c.execute('select * from suppliers')
rows=output.fetchall()
print('행의 갯수 :', len(rows))
for row in rows: 
    print('필드의 갯수 :', len(row))
    output =[]
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)

conn.close()
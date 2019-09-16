# mariaDB 설치 : https://downloads.mariadb.org/mariadb/10.4.8/

import pymysql    # 설치 : 콘솔에서 pip install pymysql

conn = pymysql.connect(host = 'localhost',
                        user = 'root',
                        password = 'qwer1234',
                        db = 'test')
c = conn.cursor()
sql = '''
    CREATE TABLE if not exists stocks
    (date text, trans text, symbol text, qty real, price real)
    '''

c.execute(sql)
sql = "insert into stocks values ('2006-03-28','buy','rhat',100,35.14)"
c.execute(sql)
conn.commit()
conn.close()
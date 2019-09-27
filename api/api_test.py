import os
import sys
import urllib.request
import json
import sqlite3

client_id = "iCfbmSA0wfvEiITT_TrQ"
client_secret = "gHEKw5vUbM"
encText = urllib.parse.quote("제주")
for i in range(1, 1000, 100):
    url = "https://openapi.naver.com/v1/search/news.json?display=100&start="+ str(i) +"&query=" + encText # json 결과
                                    # display로 데이터 건수 조절
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        data = response_body.decode('utf-8')
        c = json.loads(data)   # 문자를 읽어서 파이썬 객체로 변경
        items = c['items']
        print(items[0])
        # print(type(items))
        # print(len(items))
    else:
        print("Error Code:" + rescode)

conn = sqlite3.connect('D:/ai/pythonP/api/news.db') 
c = conn.cursor()

c.execute('''CREATE TABLE if not exists info
            (title text, link text, description text)''')
data = [[item['title'],item['link'],item['description']] for item in items]
print(data)
c.executemany('insert into info values(?, ?, ?)',data )
conn.commit()  
conn.close()

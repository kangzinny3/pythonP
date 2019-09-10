import json

customer = {
    'id' : 152352,
    'name' : '강지은',
    'history' : [
        {'date' : '2019-09-10', 'item' : 'iPhone'},
        {'date' : '2019-09-11', 'item' : 'Monitor'}
    ]
}

print(type(customer))      # class 'dict'
print(customer)

jsonResult = json.dumps(customer)    # json 형태로 저장할 때 파일이면 dump,json형태로 된 문자열이면 dumps
print(type(jsonResult))     # class 'str'
print(jsonResult)           # 한글은 유니코드 형태로 출력됨

with open('D:/ai/pythonP/json/data.json', 'wt') as f:
    json.dump(customer, f, indent=4)

cu = json.loads(jsonResult)
print(type(cu))             # class 'dict'
print(cu)

with open('D:/ai/pythonP/json/data.json', 'rt') as f:
    cu = json.load(f)
print(type(cu))             # class 'dict'  
print(cu)
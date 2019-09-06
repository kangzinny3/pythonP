'''   # 주석처리와 같은 기능
f = open('./basic/test1.txt', 'w')
for i in range(1, 11):
    data = '%d번째 줄입니다.\n' % i   # '{}번째 줄입니다.\n'.format(i)
    f.write(data)
f.close()
'''

# readline 함수 사용하기
f = open('./basic/test1.txt', 'r')
while True:
    line = f.readline()   
    if not line:
        break
    print(line) # \n + print 때문에 한 줄 씩 띄어서 출력됨 -> print(line, end='')를 해주면 이어서 출력
f.close()       # 또는 print 전에 line = line.replace('\n','')

# readlines 함수 사용하기 - 한 번에 읽어서 리스트로 반환
f = open('./basic/test1.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# read 함수 사용하기
f = open('./basic/test1.txt', 'r')
data = f.read()
print(data)
f.close()

# 파일에 새로운 내용 추가하기
f = open('./basic/test1.txt', 'a')
for i in range(11, 21 ):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()


# 이미 있는 파일을 읽을 때 
f = open('./basic/test2.txt', 'r', encoding='utf8')   # 인코딩을 맞춰줘야 함
while True:
    line = f.readline()   
    if not line:
        break
    line = line.replace('\n','')
    print(line)
f.close()

# with문과 함께 사용하기 - f.close()를 하지 않아도 됨
with open('test2.txt', 'w') as f:
    f.write('지은')

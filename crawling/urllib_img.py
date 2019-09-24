import urllib.request, os

# 1
# 이미지의 주소
url = 'https://img1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/liveboard/realfood/8c51aff9e9464e43831fed22a2c61794.jpg'

# 실행하는 파일의 경로를 찾아서 같은 경로에 이미지 저장
dirname = os.path.dirname(__file__)
savename = dirname + '/test.jpg'   # 그냥 test.jpg하면 해당폴더가 아닌 상위폴더에 저장됨

# 파일을 다운로드 받아 바로 파일로 저장
urllib.request.urlretrieve(url, savename)

# 파일을 열고 활용
mem = urllib.request.urlopen(url).read()  
# 불러온 파일을 저장
print(savename)
with open(savename, mode='wb') as f:
    f.write(mem)
    print('저장되었습니다.')


# 2
url = 'http://www.naver.com'

mem = urllib.request.urlopen(url).read()
print(mem.decode('utf-8'))   # 인코딩 방식을 UTF-8로 지정
                             # 보통 디코드에 기본값(decode())을 주고, 오류가 뜨면 맞는 값을 찾아서 넣어줌
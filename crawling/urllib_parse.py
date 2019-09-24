import urllib.parse, urllib.request


# urllib.parse.urlparse :  URL의 구문을 분석하여 6개의 구성 요소를 6 tuple로 반환
parse = urllib.parse.urlparse('192.168.147.128/bWAPP/portal.php?id=bee&pw=bug#example', scheme='http') 
print(parse)

parse = urllib.parse.urlparse('192.168.147.128/bWAPP/portal.php?id=bee&pw=bug#example', scheme='http', allow_fragments=False)
print(parse)

# urllib.parse.urlunparse() : urllib.parse.urlparse()로부터 반환된 6 tuple로부터 URL을 생성
url=urllib.parse.urlunparse(parse) 
print(url)  

# URL에서 ? 이후 부분 : sm=top_hty&fbm=0&ie=utf8&query=urllib  
parameter = {'sm':'top_hty', 'fbm':'0', 'ie':'uft8', 'query':'urllib'}
q = input('검색어입력 : ')
parameter['query'] = q
print(parameter)
data1 = urllib.parse.urlencode(parameter)
print(data1)
page = urllib.request.urlopen('http://search.naver.com/search.naver?' + data1)
print(page.read().decode())
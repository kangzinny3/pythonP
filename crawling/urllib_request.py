import urllib.request

response = urllib.request.urlopen("http://www.naver.com")
# print(response)
# print(response.geturl())
# print(response.getcode())
# print(response.info())            # 헤더의 정보
# print(response.read().decode())   # read()만 하면 인코딩이 안맞아서 한글을 읽어들이지 못함


# urllib.request.Request : urllib.request.urlopen()함수의 인자로 넘겨주기 위해, URL 요청을 인스턴트화하기 위해 사용
request = urllib.request.Request("http://www.naver.com")   
response = urllib.request.urlopen(request)
print(response.read().decode())   # byte코드를 디코딩해서 한글도 읽을 수 있도록 함
print(request.get_method())  # GET방식인것을 확인할 수 있음
request.method = 'POST'      # POST방식으로 변경
print(request.get_method()) 
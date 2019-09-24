# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')   # parser가 html종류의 문서임을 알려줌
print(soup)   # 실행해보면 </body></html>이 생김 -> html형식에 맞춰서 파싱
print(type(soup))   # html형식에 따라서 파싱된 BeautifulSoup 객체 -> 구조적 접근을 통해서 선택이 가능
print(soup.prettify())   # prettify : 구조에 맞춰서 보기 쉽게 정렬

import requests
from bs4 import BeautifulSoup  # 라이브러리 안에 있는 특정 객체만 가져오기

response = requests.get('https://makemyproject.net')
print(response)
print(response.status_code)
print(response.text)

# 위는 그냥 문자열
# 아래는 문자를 파싱해서 DOM 의 형태로 자료구조를 갖추고 있음

# html 파싱해주는 라이브러리
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
head = soup.find('head')
print('HEAD DOM:', head)

body = soup.find('body')
print('BODY DOM:', body)

if body:
    bodytext = body.text.strip()
    print('바디내용:', bodytext)
else:
    print('바디내용: body 태그를 찾을 수 없습니다')
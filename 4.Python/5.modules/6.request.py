# pip install requesets
# pip uninstall requesets

# 더이상 빌트인 모듈이 아니고 외부 라이브러리로 설치하는 것
# 외부는 어디냐 https://pypi.org/
# 파이썬 가상환경 내 라이브러리 공간에 설치됨 

import requests

response = requests.get('https://makemyproject.net')
print(response)
print(response.status_code)
print(response.text)
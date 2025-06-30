# 모듈: 하나의 파이썬 파일 - 여러개의 함수를 포함하고 있음
# 라이브러리: 모듈들의 묶음
# 프레임워크: 더 거대하게 틀과 규칙을 만들어서 따르게 하는 것

# 파이썬 공식 문서 보장

# 빌트인 모듈(추가 설치 하지 않아도 바로 쓸 수 있음) ex. datetime, ..

import datetime as dt
# 모듈명.변수명
# 모듈명.클래스명.함수명()

print(dt.MINYEAR)
print(dt.MAXYEAR)

print(dt.datetime.now())
print(dt.datetime.now().strftime('%Y-%m-%d'))
print(dt.datetime.now().strftime('%H:%M:%S'))

my_time = dt.datetime(2025, 6, 30, 10, 45, 00)
print(type(my_time))
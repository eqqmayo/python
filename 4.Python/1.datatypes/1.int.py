# 파이썬은 변수 지정하는 키워드 없음

x = 5
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)

print(x % y) # 나머지
print(x ** y)

str_x = '100'

# print(x + str_x) 문자와 숫자 더할 수 없음

int_x = int(str_x)

print('문자열 x: ', str_x)
print('int x: ', int_x)

print(x + int_x)

# 비트 연산자
print('비트연산자 AND')
print(1 & 1) # 1
print(1 & 0) # 0
print(0 & 1) # 0
print(0 & 0) # 0

print('비트연산자 OR')
print(1 | 1) # 1
print(1 | 0) # 1
print(0 | 1) # 1
print(0 | 0) # 0

# 주의사항
print(x & y) # 5 & 3 = 101 & 011 = 1
print(x | y) # 5 | 3 = 101 & 011 = 111 = 7
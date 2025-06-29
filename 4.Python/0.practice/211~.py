# 211
# 안녕
# Hi

# 212
# 7
# 15

# 213
# 함수에서 요구하는 인자를 입력하지 않고 호출

# 214
# 서로 다른 타입의 값끼리 덧셈을 할 수 없음

# 215
def print_with_smile(str):
    print(str + ':D')

# 216
print_with_smile('안녕하세요')

# 217
def print_upper_price(price):
    print(price * 1.30)

# 218
def sum(n, m):
    print(n + m)

# 219
def print_arithmetic_operation(n, m):
    print(n, '+', m, '=', n + m)
    print(n, '-', m, '=', n - m)
    print(n, '*', m, '=', n * m)
    print(n, '/', m, '=', n / m if m != 0 else 'infinity')

# 220
def print_max(n, m, k):
    max = n if n > m else m
    max = max if max > k else k
    print(max)
    
print_max(3, 10, 7)
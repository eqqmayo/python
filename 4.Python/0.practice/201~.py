# 201
from re import A


def print_coin():
    print('비트코인')

# 202
print_coin()

# 203
for _ in range(10):
    print_coin()

# 204
def print_coins():
    for _ in range(100):
        print_coin()

print_coins()

# 205
# 파이썬은 코드를 순차적으로 실행하는 인터프리터 언어이기 때문에 함수를 정의하기 전에 호출할 수 없음

# 206
# A
# B
# C
# A
# B

# 207
# A
# C
# B

# 208
# A
# C
# B
# E
# D

# 209
# B
# A

# 210
# B
# C
# B
# C
# B
# C
# A
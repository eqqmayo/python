def square_root(num):
    if num < 0:
        print('음수는 제곱근을 구할 수 없습니다')
        return None
    return num ** 0.5

def square_root2(num):
    if num < 0:
        raise ValueError('음수는 제곱근을 구할 수 없습니다')  # 내가 만든 예외
    return num ** 0.5

# print(square_root(25))
# print(square_root(1))

try:
    print(square_root2(-1))
except ValueError as e:
    print(e)
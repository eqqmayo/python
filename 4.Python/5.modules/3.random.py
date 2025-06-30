import random

print('랜덤 숫자:', random.randint(1, 100))  # 1부터 100까지 양수 다 포함하는 랜덤 숫자 생성

def roll_dice():
    return random.randint(1, 6)

print(f'주사위 던진 결과: {roll_dice()}')

# 주사위를 n번 던져서 각 숫자가 나올 확률 출력
def get_probability(n):
    # 1. dict.fromkeys() 사용
    count = dict.fromkeys(range(1, 7), 0)

    # 2. 딕셔너리 컴프리헨션
    # count2 = {i: 0 for i in range(1, 7)}

    for _ in range(n):
        result = roll_dice()
        count[result] += 1

    for i in range(1, 7):
        print(f'{i}이 나온 횟수: {count[i]}번, 확률: {count[i] / 10 * 100}%')

get_probability(100_000)
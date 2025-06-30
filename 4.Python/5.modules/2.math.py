import math
print(math.pi)

# 원의 넓이
radius = 5
area = math.pi * radius ** 2
area = math.pi * math.pow(radius, 2)

print(f'반지름이 {radius}인 원의 넓이는 {area:.2f} 입니다') # 소수 둘째자리까지 표시

text = 'hi'
print(f'[{text:<10}]')
print(f'[{text:>10}]')
print(f'[{text:^10}]')
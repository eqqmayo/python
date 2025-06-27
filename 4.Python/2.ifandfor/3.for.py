for i in range(5):
    print(i)

for i in range(1, 5):  # 끝 값은 포함하지 않는다
    print(i)

for i in range(1, 10, 2):  # 1부터 10까지 2칸씩 건너뛴다
    print(i)


fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)

for i, f in enumerate(fruits):
    print(i, f)

str = 'hello, python'

for char in str:
    print(char)

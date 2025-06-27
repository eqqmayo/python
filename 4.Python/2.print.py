name = 'Alice'
print(name)
print('hello', name) # 인자로 받으면 띄어쓰기 O
print('hello' + name) # 덧셈 연산은 띄어쓰기 X

name1 = 'Bob'
name2 = 'Charlie'
print('hello {}'.format(name))
print('hello {} and {}'.format(name1, name2))
print('hello {1} and {0}'.format(name1, name2))

print('Hello, %s' % name)
print('Hello, %s %s' % (name1, name2))

# 현재 가장 많이 쓰는 표기법
print(f'hello {name}')

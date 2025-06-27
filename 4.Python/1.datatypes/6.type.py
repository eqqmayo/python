x = 1
y = 'abc'
z = [1, 2, 3]


print(type(x))
print(type(y))
print(type(z))

print(isinstance(x, int))
print(isinstance(y, int))

print(isinstance(y, (int, str))) # int or str


class A():
    pass     # 일단 비워둠

class B(A):  # B extends A (A 상속받음)
    pass

class C():
    pass

b = B()
print(isinstance(b, A))  # true
print(isinstance(b, B))  # true
print(isinstance(b, C))  # false

a = A()
print(isinstance(a, A))  # true
print(isinstance(a, B))  # false
print(isinstance(a, C))  # false
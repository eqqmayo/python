class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property  # 데코레이터는 처음에 주석 목적이었으나, 지금은 기능이 더해짐. 
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property 
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        if age >= 0:
            self._age = age
        else:
            print('나이는 0보다 커야함')

    def greet(self):
        print(f'hello, 저는 {self._name} 입니다')
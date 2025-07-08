class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # 객체를 사람들이 보기 좋게 표현하는 함수
        return f'Person(name={self.name}, age={self.age})'

    def __eq__(self, other):  # 나와 다른 객체를 비교할때의 조건
        return self.name == other.name and self.age == other.age

    def greet(self):
        print(f'hello, 저는 {self.name} 입니다')

    def ride_car(self):
        print('부릉부릉')

person1 = Person('eqqmayo', 22)
person2 = Person('calia', 28)
person3 = Person('calia', 28)
person4 = person3

person1.greet()
person1.ride_car()

person2.greet()
person2.ride_car()

print(person1)
print(person1 == person2)
print(person2 == person3)
print(person3 == person4)
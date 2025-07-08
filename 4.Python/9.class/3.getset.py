class Person:
    def __init__(self, name, age):
        self._name = name  # protected
        self.__age = age  # private - 클래스 밖에서 접근 못함
    
    @property  # 이 함수는 getter 입니다
    def name(self):
        return self._name

    @name.setter  # 이 함수는 setter 입니다
    def name(self, name):
        self._name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print('나이는 0보다 커야함')

    def greet(self):
        print(f'hello, 저는 {self._name} 입니다')

    def ride_car(self):
        print('부릉부릉')

person1 = Person('eqqmayo', 22)  
person2 = Person('calia', 28)

person1.name = 'jhyun'  # 데코레이터로 지정했으면 함수가 아닌 변수처럼 접근 가능; 변수를 자유롭게 변경하는 것처럼 보이지만 실제로는 함수통해서 변경하는 것

print(person1.name)
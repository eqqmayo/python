class Person:
    _count = 0  # 클래스 변수 (공통, 공용 영역에 해당), private, protected

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person._count += 1

    # getter, setter:  내부 변수에 저장해서 값을 읽어올때는 getter 사용 / 내부 변수에 셋팅할때는 setter

    def greet(self):
        print(f'hello, 저는 {self.name} 입니다')

    def ride_car(self):
        print('부릉부릉')

    @classmethod  # 데코레이터 - 나의 함수에 기능을 더해주는것
    def get_count(cls):  # 클래스 자체에 접근하기 위해 cls 라는 클래스 자신을 칭하는 인자를 받아온다
        return cls._count

    # def set_count(cls, count): 
    #     cls._count = count

person1 = Person('eqqmayo', 22)  # 객체를 찍어내는 과정 = 실체화 = instantiation
person2 = Person('calia', 28)

print(person1._count)
print(person1.get_count()) # XXX
print(Person.get_count()) # OOO





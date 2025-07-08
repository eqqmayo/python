from person import Person
from student import Student
from employee import Employee

alice = Person('alice', 22)
bob = Person('bob', 24)
theo = Student('theo', 21, 1717)
erik = Employee('erik', 26, 'AMD')

alice.greet()
bob.greet()

bob.name = 'BOB'
bob.greet()

theo.greet()
theo.study()

erik.greet()
erik.work()
from person import Person

class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)  # 부모 객체를 불러 그 곳을 통해 초기화
        self._company = company

    def greet(self):  # 사람 인사 대신 나만의 인사를 할거야: 메서드 오버라이딩
        print(f'저는 {self._company}에서 일하는 {self._name} 입니다')

    def work(self):
        print(f'{self._company}에서 일하는 중')

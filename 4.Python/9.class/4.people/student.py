from person import Person

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # 부모 객체를 불러 그 곳을 통해 초기화
        self._student_id = student_id

    def study(self):
        print(f'{self.name}은 학교에서 공부중')

# 251
# 클래스: 객체/인스턴스를 만드는 틀, 설계도
# 객체: 클래스로부터 생성된 실체
# 인스턴스: 클래스로부터 생성된 실체

# 252 ~ 259
class Human:
    def __init__(self, name, age, gender):
        print('응애응애')
        self.name = name
        self.age = age
        self.gender = gender
    
    def who(self):
        print(f'이름: {self.name}, 나이: {self.age}, 성별: {self.gender}')

    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self):
        print('나의 죽음을 알리지 말라')

areum = Human('아름', 25, '여자')

print(areum.name)
print(areum.age)
print(areum.gender)

areum.who()

del areum

# 260
# 함수 정의시 self 누락
# 파이썬은 클래스의 인스턴스 메서드를 호출할때 첫번째 인자로 인스턴스 자신을 전달하기 때문에
# 반드시 첫번째 인자로 self를 받아야 함
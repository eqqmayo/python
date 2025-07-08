from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._hp: int = 100

    @abstractmethod  # 이 클래스를 상속받는 클래스는 강제적으로 구현
    def speak(self) -> None:
        print('blahblah')

    @abstractmethod
    def move(self) -> None:
        if self._hp == 0:
            print('더이상 움직일 수 없음')
            return
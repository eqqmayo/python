class Animal:
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._hp: int = 100

    def speak(self) -> None:
        print('blahblah')

    def move(self) -> None:
        if self._hp == 0:
            print('더이상 움직일 수 없음')
            return
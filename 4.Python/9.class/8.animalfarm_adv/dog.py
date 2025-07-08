from animal import Animal

class Dog(Animal):
    def speak(self) -> None:
        print('Woof')

    def move(self) -> None:
        super().move()
        self._hp = max(0, self._hp - 10)

from animal import Animal

class Cat(Animal):
    def speak(self) -> None:
        print('Meow')

    def move(self) -> None:
        super().move()
        self._hp = max(0, self._hp - 5)


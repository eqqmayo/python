from typing import List
from animal import Animal

class Farm:
    def __init__(self) -> None:
        self._animals: List[Animal] = []

    def add_animal(self, animal: Animal) -> None:
        self._animals.append(animal)

    def feed_all(self) -> None:
        for animal in self._animals:
            animal._hp += 50

    def play_all(self) -> None:
        for animal in self._animals:
            if animal._hp == 0:
                print(f'{animal._name} 에너지 없음')
            else:
                animal._hp = max(0, animal._hp - 10)

    def show_all(self) -> None:
        for animal in self._animals:
            print(f'이름: {animal._name}, 에너지: {animal._hp}')


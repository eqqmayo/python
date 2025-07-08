from cat import Cat
from dog import Dog
from farm import Farm
from panda import Panda

if __name__ == '__main__':

    cat1 = Cat('cat1')
    cat2 = Cat('cat2')
    dog1 = Dog('dog1')
    dog2 = Dog('dog2')

    cat1.speak()
    dog1.speak()

    # pythonic
    for _ in range(11):
        dog1.move()
        cat1.move()

    my_farm = Farm()

    my_farm.add_animal(cat1)
    my_farm.add_animal(cat2)
    my_farm.add_animal(dog1)
    my_farm.add_animal(dog2)

    my_farm.play_all()
    my_farm.feed_all()
    my_farm.show_all()

    panda = Panda('panda')

    panda.move()
    panda.speak()

import random
import datetime
from common import get_uuid, get_address

class StoreGenerator:
    def __init__(self):
        self.uuid = get_uuid()
        self.name = self.generate_name("data/town.txt")
        self.type = self.generate_type("data/storetype.txt")
        self.address = get_address()

    def generate_name(self, town_file: str) -> str:
        with open(town_file, 'r') as file:
            towns = file.read().splitlines()

        return self.type + ' ' + random.choice(towns) + str(random.randint(1, 10)) + '호점'

    def generate_type(self, type_file: str) -> str:
        with open(type_file, 'r') as file:
            types = file.read().splitlines()
        return random.choice(types)
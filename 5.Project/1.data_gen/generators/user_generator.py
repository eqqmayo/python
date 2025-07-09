from name_generator import NameGenerator
from birthdate_generator import BitrthdateGenerator
from gender_generator import GenderGenerator
from address_generator import AddressGenerator

class UserGenerator: 
    def __init__(self):
        self.name_gen = NameGenerator('names.txt')
        self.bday_gen = BitrthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator('cities.txt')

    def generate_user(self, count):
        users = []
        for _ in range(count):
            name = self.name_gen.generate_name()
            bday = self.bday_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            address = self.address_gen.generate_address()
            users.append((name, bday, gender, address))
        return users
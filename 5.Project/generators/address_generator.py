import random

class AddressGenerator:
    def __init__(self, file_path) -> None:
        self.cities = self.load_data_from_file(file_path)

    def load_data_from_file(self, file_path):
        with open(file_path, 'r') as file:
            data = file.read().splitlines() 
        return data

    def generate_address(self):
        city = random.choice(self.cities)
        street_num = random.randint(1, 100)
        return f'{street_num} {city}'
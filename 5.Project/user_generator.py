import random
import datetime
from common import get_uuid, get_address

class UserGenerator:
    def __init__(self):
        self.uuid = get_uuid()
        self.name = self.generate_name("data/firstname.txt", "data/lastname.txt")
        self.gender = self.generate_gender()
        self.birthdate = self.generate_birthdate(1970, 2010)
        self.age = self.get_age(self.birthdate)
        self.address = self.generate_address()

    def generate_name(self, fname_file: str, lname_file: str) -> str:
        with open(fname_file, 'r') as file:
            firstnames = file.read().splitlines()
        with open(lname_file, 'r') as file:
            lastnames = file.read().splitlines()

        return random.choice(lastnames) + random.choice(firstnames)

    def generate_gender(self) -> str:
        return random.choice(["Male", "Female"])

    def generate_birthdate(self, start_year: int, end_year: int) -> str:
        start_date = datetime.date(start_year, 1, 1)
        end_date = datetime.date(end_year, 12, 31)

        diff = (end_date - start_date).days
        random_days = random.randint(0, diff)
    
        return f'{start_date + datetime.timedelta(days=random_days)}'

    def get_age(self, birthdate: str) -> int:
        birth = datetime.datetime.strptime(birthdate, '%Y-%m-%d').date()
        today = datetime.date.today()

        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    def generate_address(self) -> str:
        return get_address()
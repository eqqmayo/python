import uuid
import random
import csv

def get_uuid() -> str:
    return str(uuid.uuid4())

def get_address() -> str:
    with open('data/city.txt', 'r') as file:
        city = random.choice(file.read().splitlines())
    with open('data/district.txt', 'r') as file:
        district = random.choice(file.read().splitlines())
    return f'{city} {district} {random.randint(1, 99)}{random.choice(["길", "로"])} {random.randint(1, 99)}'

def generate_csv(generator, columns: list[str], count: int, filename: str) -> None:
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        for _ in range(count):
            user = generator()
            writer.writerow([getattr(user, col) for col in columns])
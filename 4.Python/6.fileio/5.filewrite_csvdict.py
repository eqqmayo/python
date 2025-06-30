# csv: comma seperated value
import csv

file_path = 'test.csv'

data = [
    {'Name': 'Alice', 'Age': 23, 'City': 'Seoul'},
    {'Name': 'Bob', 'Age': 33, 'City': 'Busan'},
    {'Name': 'Charlie', 'Age': 22, 'City': 'Jeju'},
]

for person in data:
    print(person)
    for key, value in person.items():
        print(f'key: {key}, value: {value}')

with open(file_path, 'w', newline='') as file:
    # headers = ['Name', 'Age', 'City']
    headers = data[0].keys()
    csv_writer = csv.DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerows(data)

print('csv 쓰기 완료')
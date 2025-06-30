# csv: comma seperated value
import csv

file_path = 'test.csv'

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 23, 'Seoul'],
    ['Bob', 33, 'Busan'],
    ['Charlie', 22, 'Jeju']
]

for i in range(len(data)):
    print(data[i])

with open(file_path, 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
    csv_writer.writerow(['Calia', 38, 'Daegu'])

print('csv 쓰기 완료')
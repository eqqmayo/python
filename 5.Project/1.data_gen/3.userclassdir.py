import sys
from generators.user_generator import UserGenerator

class DisplayData(UserGenerator):
    def print_data(self, count):
        data = self.generate_user(count)
        for name, bday, gender, address in data:
            print(name, bday, gender, address)


# 최종 실행
print(sys.argv)  # 입력 인자
# sys.argv[0]  # 여기는 실행 파일명 자신
# sys.argv[1]  # 첫번째 인자

output_format = 'console'
if len(sys.argv) > 1:
    num_data = int(sys.argv[1])
else:
    num_data = input('원하는 데이터 갯수 입력: ')

my_data = DisplayData()
if output_format == 'console':
    pass
# my_data.print_data(num_data)
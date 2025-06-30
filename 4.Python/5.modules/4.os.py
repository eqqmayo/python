import os

# 현재 디렉토리 가져오기 current working directory
print(os.getcwd())

# 시스템콜
# 하드웨어에 대한 모든 접근은 os가 하겠다

# 디렉토리 만들기
my_directory = 'my_directory'

os.mkdir(my_directory)
print('생성완료')

# 디렉토리 이동
os.chdir(my_directory)
print('이동완료')

os.chdir('..')  # . 은 현재 디렉토리 .. 은 부모 디렉토리
print('부모 디렉토리로 이동완료')

# 디렉토리 삭제
os.rmdir(my_directory)
print('삭제완료')

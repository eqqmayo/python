file_path = 'test.txt'

# 파일을 읽을 때의 '모드'
# r = read, w = write(새로쓰기), a = append(이어서쓰기)

# with open(file_path, 'r') as file:
with open(file_path, 'r', encoding='utf-8') as file:  # 파일이 열려있는 동안
    contents = file.read()    # 수행하고 파일 닫힘

print('파일 내용:', contents)

# cp949: 윈도우가 한글 표현에 사용하는 포맷
# utf-8: 지금 시대의 표준화 되어 있는 유니코드
file_path = 'test.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    file.write('hello!\n')  # \n 뉴라인 - 줄바꿈 캐릭터
    file.write('안녕!')
    file.write('\n바이!')

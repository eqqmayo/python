
try:
    with open('hello.txt', 'r') as file:
        contents = file.read()

    print('파일내용:', contents)
except FileNotFoundError:
    print('파일 존재하지 않음')
except:
    print('알 수 없는 오류')
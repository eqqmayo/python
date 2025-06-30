import os
import zipfile
# 빌트인 모듈중 zip 으로 압축해주는 기능 있음

my_dir = 'my_directory'

# 디렉토리 내 파일 읽어오기
for filename in os.listdir(my_dir):
    file_path = os.path.join(my_dir, filename)
    if (os.path.isfile(file_path)):
        print(filename)
        print(file_path)

        zip_filename = f'{filename}.zip'

        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            zipf.write(file_path, arcname=filename)
            print('압축완료')
            
        # 원본 파일 삭제
        os.remove(file_path)
        print('파일 삭제')


    # 비트코인 .. . .
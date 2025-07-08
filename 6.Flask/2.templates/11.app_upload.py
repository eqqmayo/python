from click import File
from flask import Flask, make_response, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
# ALLOWED_FILE_EXT = ['png', 'jpg', 'jpeg', 'gif']
ALLOWED_FILE_EXT = {'png', 'jpg', 'jpeg', 'gif', 'png'}  # pythonic 한 자료구조

os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # 시작할때 폴더가 없으면 만들어주기

def allowed_file(filename):
    if '.' not in filename:
        return False

    ext = filename.rsplit('.', 1)[-1].lower()

    if ext in ALLOWED_FILE_EXT:
        return True
    else:
        return False

def allowed_file_pythonic(filename):
    return '.' in filename and filename.rsplit('.', 1)[-1].lower() in ALLOWED_FILE_EXT

@app.route('/')  
def index():
    return render_template('upload.html') 

def get_file_size(file):
    pos = file.stream.tell()  # (이전 작업을 고려해서) 현재 Fd의 위치를 저장
    file.stream.seek(0, os.SEEK_END) # 끝으로 이동
    size = file.stream.tell()  # 너의 위치 기반으로 크기 알려줘
    file.stream.seek(pos) # 원래 위치로 이동
    return size

# def get_file_size(file):
#     file.stream.seek(0, os.SEEK_END)
#     size = file.tell()  # 너의 현재 위치
#     file.seek(0)  # 다시 처음 위치로 이동
#     return size

@app.route('/upload', methods=['POST'])  
def upload_file():
    print(request.form)  # 이전에 받아온건 파일명만을 받아왔음
    print(request.files)  # 실제로 파일 내용까지 FileStorage라는 객체 형태로 받아옴

    file = request.files['file']
    
    if file.filename == '':
        return make_response('파일이 올바르게 전송되지 않음')

    # 비즈니스 로직 - 내가 정한 프로세싱 룰들을 여기에 하나둘씩 구현

    # 2. 용량이 1MB 보다 크면 허용하지 않는다
    file_size = get_file_size(file)
    max_size = 1 * 1024 * 1024  # 1MB = 1KB가 1024개인 것. 1KB는 1바이트가 1024개
    if file_size > max_size:
        return '파일 용량이 너무 큽니다. 1MB 이하의 파일만 업로드 가능'

    # 1. 사진 파일만 업로드 가능하게 한다
    if allowed_file_pythonic(file.filename):
        # 파일 저장하기 - 현재 폴더의 uploads 폴더 안에 받은 파일 저장
        if file.filename:  # None이 아닌 경우에만 저장
            filepath = os.path.join('./', UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            print(os.listdir(UPLOAD_FOLDER))
            return render_template('upload.html', files=os.listdir(UPLOAD_FOLDER)) 
    else:
        return make_response('허용되지 않는 파일입니다.')

    return make_response('파일이 올바르게 전송되지 않음')

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    if filename:
        filepath = os.path.join('./', UPLOAD_FOLDER, filename)
        if os.path.exists(filepath):
            os.remove(filepath)
 
    # return render_template('upload.html', files=os.listdir(UPLOAD_FOLDER))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 

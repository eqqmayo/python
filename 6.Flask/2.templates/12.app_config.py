from click import File
from flask import Flask, make_response, render_template, request
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_FILE_EXT'] = {'png', 'jpg', 'jpeg', 'gif', 'png'}
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True) 

def allowed_file(filename):
    if '.' not in filename:
        return False

    ext = filename.rsplit('.', 1)[-1].lower()

    if ext in app.config['ALLOWED_FILE_EXT']:
        return True
    else:
        return False

def allowed_file_pythonic(filename):
    return '.' in filename and filename.rsplit('.', 1)[-1].lower() in app.config['ALLOWED_FILE_EXT']

@app.route('/')  
def index():
    return render_template('upload.html') 

@app.route('/upload', methods=['POST'])  
def upload_file():
    file = request.files['file']
    
    if file.filename == '':
        return make_response('파일이 올바르게 전송되지 않음')

    # 비즈니스 로직 - 내가 정한 프로세싱 룰들을 여기에 하나둘씩 구현

    # 2. 용량이 1MB 보다 크면 허용하지 않는다
    # 용량크면 MAX_CONTENT_LENGTH 가 동작해서 자동으로 예외 발생 시킴
    # 이런 것들은 Flask 프레임워크 내에서 알아서 잘 해줌

    # 1. 사진 파일만 업로드 가능하게 한다
    if allowed_file_pythonic(file.filename):
        if file.filename: 
            filepath = os.path.join('./', app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            print(os.listdir(app.config['UPLOAD_FOLDER']))
            return render_template('upload.html', files=os.listdir(app.config['UPLOAD_FOLDER'])) 
    else:
        return make_response('허용되지 않는 파일입니다.')

    return make_response('파일이 올바르게 전송되지 않음')

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    if filename:
        filepath = os.path.join('./', app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(filepath):
            os.remove(filepath)
 
    return render_template('upload.html', files=os.listdir(app.config['UPLOAD_FOLDER']))

# 413 발생 시의 오류 핸들러를 커스텀으로 등록
# 플라스크 프레임워크를 잘 사용하는 방법
@app.errorhandler(413)
def too_large(e):
    size_mb = app.config['MAX_CONTENT_LENGTH'] / (1024 * 1024)
    return f'업로드 파일이 너무 큽니다. 최대 {size_mb}MB 까지만 허용'
if __name__ == '__main__':
    app.run(debug=True) 

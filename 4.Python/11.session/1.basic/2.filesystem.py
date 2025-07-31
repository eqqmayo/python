from flask import Flask, session
from flask_session import Session
import os

app = Flask(__name__)
app.secret_key = 'asdf'

app.config['SESSION_TYPE'] = 'filesystem'  # 기본값이 null, 서버에 저장하지 않음. 그 외 filesystem / redis / mongodb / sqlalchemy 등등
app.config['SESSION_FILE_DIR'] = os.path.join(os.getcwd(), 'my_sessions')
# app.config['SESSION_FILE_DIR'] = './my_sessions'
app.config['SESSION_PERMANENT'] = False # False 면 브라우저가 닫히면 삭제
app.config['SESSION_USER_SIGNER'] = True # 세션 쿠키에 서명 사용 여부

Session(app) # 우리 app 에 세션 기능 더해줌

@app.route('/set-session/<username>')
def set_session(username):
    session['username'] = username
    return '세션이 저장됨'

@app.route('/get-session')
def get_session():
    if 'username' in session:
        return f'세션정보 {session['username']}'
    else:
        return '저장된 정보 없음'

@app.route('/clear-session')
def del_session():
    session.pop('username', None)
    return '세션정보 삭제됨'

if __name__ == '__main__':
    app.run(debug=True)
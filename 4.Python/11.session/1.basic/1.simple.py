from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'my-secret-key'  # 세션 암호화를 위한 키 (내가 관리하고, 암호화/복호화하고, 외부에 노출되면 안됨)

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
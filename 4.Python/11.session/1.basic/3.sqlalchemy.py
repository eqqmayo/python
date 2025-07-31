from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'asdf'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sessions.db'
db = SQLAlchemy(app)

app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db
Session(app)

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
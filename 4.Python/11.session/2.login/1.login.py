from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'blahblah'

users = [
    {'name': 'Alice', 'id': 'alice', 'password': 'alice'},
    {'name': 'Bob', 'id': 'bob', 'password': 'bob'},
    {'name': 'Charlie', 'id': 'charlie', 'password': 'charlie'},
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')

        user = next((u for u in users if u['id'] == id and u['password'] == password), None)
        if user:
            session['user'] = user
            return redirect(url_for('dashboard'))
        else:
            return '로그인 실패'
    else:
        if session.get('user'):
            return redirect(url_for('dashboard'))

    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    user = session.get('user') # 아까 우리가 저장한 정보
    if user:
        return render_template('dashboard.html', username=user['name'])
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

# 미션1: 로그인된 사용자는 dashboard.html 만들어서 '안녕하세요, OOO님' 세션에 있는 정보 기반으로
# 미션2: / 에 접속해서 로그인된 사용자면 바로 dashboard로 보내기
# 미션3: 로그아웃 구현하기 '안녕하세요, OOO님' 아래 '로그아웃' 추가 a href /logout

if __name__ == '__main__':
    app.run(debug=True)
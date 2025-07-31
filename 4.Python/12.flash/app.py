from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'sdfsd'

users = [
    {'name': 'Alice', 'id': 'alice', 'password': 'alice'},
    {'name': 'Bob', 'id': 'bob', 'password': 'bob'},
    {'name': 'Charlie', 'id': 'charlie', 'password': 'charlie'},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form.get('id')
        pw = request.form.get('pw')

        user = next((u for u in users if u['id'] == id and u['pw'] == pw), None)
        if user:
            session['user'] = user
            flash('로그인 성공', "success")
            return redirect(url_for('user'))

        flash('로그인 실패')
        return redirect(url_for('home'))
    else:
        if 'user' in session:
            flash('이미 로그인된 사용자', "warning")
            return redirect(url_for('user'))

        return redirect(url_for('home'))

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        flash('정상적으로 로그아웃', "success")
        return render_template('user.html', username=user['name'])
            
    flash('비정상 접근, 로그인 필요', "warning")
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        flash('정상적으로 로그아웃', "success")
    else:
        flash('이미 로그아웃함', "warning")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

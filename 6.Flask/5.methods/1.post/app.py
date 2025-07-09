from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 3명 이상 사용자(이름, 아이디, 암호) > 로그인할때 id/pw 맞는지 체크 > 맞으면 성공페이지로 이동 / 실패하면 로그인 실패 출력
users = [
    { 'name': '고양이', 'id': 'cat', 'pw': 'cattt'},
    { 'name': '강아지', 'id': 'dog', 'pw': 'doggg'},
    { 'name': '참새', 'id': 'bird', 'pw': 'birddd'},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # POST
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']

        # user = next((u for u in users if u['id'] == id and u['pw'] == pw), None)
        # if user:
        #     return '로그인 성공'
        # else:
        #     return '로그인 실패'

        for user in users:
            if user['id'] == id and user['pw'] == pw:
                name = user['name']
                return redirect(url_for('user', name=name))
        return redirect(url_for('login'))

    # GET
    else:
        return render_template('login.html')
        # return render_template('user.html', user=user)
        # return redirect('/user')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/user/<name>')
def user(name=None):  # 초기값 할당
    return render_template('user.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# db 안쓸때는,,
users = []
next_id = 1

@app.route('/', methods=['GET', 'POST'])
def index():
    global next_id  # 글로벌 변수에 write 할때는 글로벌 선언 필요

    if request.method == 'POST':
        # POST 요청 처리
        name = request.form['name']
        age = int(request.form['age'])

        # 사용자 추가
        users.append({'id': next_id, 'name': name, 'age': age})
        next_id += 1  # 자동 증가

        return redirect('/')  # 추가 끝났으면 그 페이지 다시 불러오기

    # GET 요청 처리
    return render_template('index.html', users=users)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            break
    return redirect('/')

@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    for user in users:
        if user['id'] == user_id:
            if request.method == 'POST':
                user['name'] = request.form['name']
                user['age'] = int(request.form['age'])
                break
            # GET
            return render_template('update_user.html', user=user)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, redirect, render_template, request
import database as db

app = Flask(__name__)

users = []
next_id = 1

@app.before_request
def initialise():
    db.create_table()

@app.route('/', methods=['GET', 'POST'])
def index():
    global users
    global next_id  # 글로벌 변수에 write 할때는 글로벌 선언 필요

    if request.method == 'POST':
        # POST 요청 처리
        name = request.form['name']
        age = int(request.form['age'])

        # 사용자 추가
        users.append({'id': next_id, 'name': name, 'age': age})
        db.insert_user(name, age)
        next_id += 1  # 자동 증가

        return redirect('/')  # 추가 끝났으면 그 페이지 다시 불러오기

    # GET 요청 처리
    users = db.get_users()
    return render_template('index.html', users=users)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            db.delete_user_by_id(user_id)
            break
    return redirect('/')

@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    for user in users:
        if user['id'] == user_id:
            if request.method == 'POST':
                new_name = request.form['name']
                new_age = int(request.form['age'])

                user['name'] = new_name
                user['age'] = new_age
                db.update_user_by_id(id, new_name, new_age)
                break
            # GET
            return render_template('update_user.html', user=user)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)  # 디버그 모드에서는 메인함수가 두번 불릴 수 있다

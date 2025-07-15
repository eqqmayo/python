from flask import Flask, redirect, render_template, request
from models import db, User

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
    db.init_app(app)
    return app

app = create_app()

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    age_str = request.form.get('age')
    
    if not name or not age_str:
        return redirect('/')  # 필수 값이 없으면 돌아감
    
    try:
        age = int(age_str)
    except ValueError:
        return redirect('/')  # 숫자 변환 실패시 돌아감

    new_user = User(name=name, age=age)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_user(id):
    user = db.session.get(User, id)
    if user:
        db.session.delete(user)
        db.session.commit()
    else:
        print('사용자 없음')

    return redirect('/')  # redirect(url_for('index')) 가 좀 더 나음

@app.route('/update_user/<int:id>')
def update_user():
    user = db.session.get(User, id)

    name = request.form.get('name')
    age = request.form.get('age')

    if user and name and age:
        user.name = name
        user.age = int(age)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
from app import create_app
from models import db, User

app = create_app()

# 테이블 생성(초기화)
with app.app_context():  # 앱이 생성되고 초기화되어 준비가 되었을때
    db.drop_all()  # 모든 테이블 삭제
    db.create_all()  # 새로 초기화

    db.session.add(User(name='Alice', age=30))
    db.session.add(User(name='Bob', age=25))
    db.session.add(User(name='Charlie', age=20))
    db.session.commit()

    for u in User.query.all():
        print(u.id, u.name, u.age)
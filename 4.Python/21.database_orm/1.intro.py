from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('mysql:///example.db')
engine = create_engine('sqlite:///example.db')  # 상대경로: 상대경로로 설정하면 기본디렉토리는 instance 라는 폴더
# engine = create_engine('sqlite:///tmp/example.db')  # 절대경로
# engine = create_engine('sqlite:///./example.db')  # 절대경로

# Base 클래스를 만들어서 DB랑 객체랑 연결
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'  # 테이블명을 내가 지정하고 싶을 때(옵셔널)
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# DB 에게 테이블 생성하라고 시킴
Base.metadata.create_all(engine)

# 세션 통해서 실제 DB와 CRUD를 함
Session = sessionmaker(bind=engine)
sess = Session()  # 커서 같은 것

# INSERT INTO users (name, age) VALUES ('Alice', 30);
new_user = User(name='Alice', age=30)
sess.add(new_user)
sess.commit()

# SELECT * FROM users;
users = sess.query(User).all()
# print(users)
for user in users:
    print(user.id, user.name, user.age)



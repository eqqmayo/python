from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import Session as s

engine = create_engine('sqlite:///users.db')

Base = declarative_base()

# 테이블 설계 - 객체 설계
# 사용자 '모델' 정의
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sess = Session()

# CRUD 함수 만들기
def create_user(session: s, name: str, age: int) -> User:
    user = User(name=name, age=age)
    session.add(user)
    session.commit()
    return user

def get_users(session: s) -> list[User]:
    users = session.query(User).all()
    return users

def get_user_by_id(session: s, user_id: int) -> User:
    # user = session.query(User).filter_by(id=user_id).first()
    # return user
    return session.get(User, user_id)  # 2.x 부터 새롭게 등장

def update_user_age(session: s, user_id: int, new_age: int) -> bool:
    user = get_user_by_id(session, user_id)
    if not user:
        return False
    
    user.age = new_age
    session.commit()
    return True

def delete_user_by_id(session: s, user_id: int) -> bool:
    # sess.query(User).filter(User.id == user_id).delete(synchronize_session=False)
    user = get_user_by_id(session, user_id)
    if not user:
        return False
    
    session.delete(user)
    session.commit()
    return True

def delete_user_by_name(session: s, name: str) -> bool:
    users = session.query(User).filter_by(name=name).all()
    if not users:
        return False
    
    for user in users:
        session.delete(user)

    session.commit()
    return True
    
if __name__ == '__main__':
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    with Session() as sess:
        alice = create_user(sess, 'Alice', 30)
        bob = create_user(sess, 'Bob', 25)
        print(f'추가된 사용자: {alice.id}, {bob.id}')

        user1 = get_user_by_id(sess, alice.id)  # type: ignore
        print('조회한 사용자 정보:', user1.name, user1.age)

        user2 = get_user_by_id(sess, bob.id)  # type: ignore
        print('조회한 사용자 정보:', user2.name, user2.age)

        update_alice = update_user_age(sess, alice.id, 29)  # type: ignore
        print('업데이트 성공 실패 여부 확인:', update_alice)

        users = get_users(sess)
        for u in users:
            print(u.id, u.name, u.age)

        delete_alice = delete_user_by_id(sess, alice.id)  # type: ignore
        print('삭제 성공 실패 여부 확인:', delete_alice)

        users = get_users(sess)
        for u in users:
            print(u.id, u.name, u.age)
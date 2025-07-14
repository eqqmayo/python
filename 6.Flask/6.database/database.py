import sqlite3

MY_DATABASE = 'example.db'

# db에 접속하는 함수를 작성하시오.
def connect_db():
    conn = sqlite3.connect(MY_DATABASE)
    conn.row_factory = sqlite3.Row  # 각각의 행이 튜플이 아니라 딕셔너리로 cast 가능한 Row 로 반환됨
    return conn

# 테이블 생성함수 작성하시오.
def create_table():
    conn =  connect_db()
    cur = conn.cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()
    
# 데이터 삽입 함수
def insert_user(name, age):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    
    conn.commit()
    conn.close()
    
# 데이터 조회 함수
def get_users():
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    
    conn.commit()
    conn.close()
    
    return [{'id': user[0], 'name': user[1], 'age': user[2]} for user in users]

def get_user_by_name(name):
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute('SELECT * FROM users WHERE name = ?', (name, ))
    user = cur.fetchall()
    
    conn.commit()
    conn.close()
    
    return user

# 데이터 수정 함수
def update_user_by_id(id, new_name, new_age):
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute('UPDATE users SET name = new_name AND age = ? WHERE id = ?', (id, new_name, new_age))
    
    conn.commit()
    conn.close()
    
def delete_user_by_name(name):
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute('DELETE FROM users WHERE name = ?', (name, ))
    
    conn.commit()
    conn.close()
    
def delete_user_by_age(age):
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute('DELETE FROM users WHERE age = ?', (age, ))
    
    conn.commit()
    conn.close()
    
def delete_user_by_id(id):
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute('DELETE FROM users WHERE id = ?', (id, ))
    
    conn.commit()
    conn.close()

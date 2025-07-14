# import mysql.connector
# from mysql.connector import Error

# # MySQL 데이터베이스 연결 설정
# DB_CONFIG = {
#     'host': 'localhost',
#     'database': 'example_db',
#     'user': 'your_username',
#     'password': 'your_password',
#     'port': 3306
# }

# # db에 접속하는 함수
# def connect_db():
#     try:
#         conn = mysql.connector.connect(**DB_CONFIG)
#         return conn
#     except Error as e:
#         print(f"Error connecting to MySQL: {e}")
#         return None

# # 테이블 생성함수
# def create_table():
#     conn = connect_db()
#     if conn is None:
#         return
    
#     cur = conn.cursor()
    
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             name VARCHAR(255) NOT NULL,
#             age INT NOT NULL
#         )
#     ''')
    
#     conn.commit()
#     cur.close()
#     conn.close()

# # 데이터 삽입 함수
# def insert_user(name, age):
#     conn = connect_db()
#     if conn is None:
#         return
    
#     cur = conn.cursor()
    
#     cur.execute('INSERT INTO users (name, age) VALUES (%s, %s)', (name, age))
    
#     conn.commit()
#     cur.close()
#     conn.close()

# # 데이터 조회 함수
# def get_users():
#     conn = connect_db()
#     if conn is None:
#         return []
    
#     cur = conn.cursor()
    
#     cur.execute('SELECT * FROM users')
#     users = cur.fetchall()
    
#     cur.close()
#     conn.close()
    
#     return users

# def get_user_by_name(name):
#     conn = connect_db()
#     if conn is None:
#         return []
    
#     cur = conn.cursor()
    
#     cur.execute('SELECT * FROM users WHERE name = %s', (name,))
#     user = cur.fetchall()
    
#     cur.close()
#     conn.close()
    
#     return user

# # 데이터 수정 함수
# def update_user_age(name, new_age):
#     conn = connect_db()
#     if conn is None:
#         return
    
#     cur = conn.cursor()
    
#     cur.execute('UPDATE users SET age = %s WHERE name = %s', (new_age, name))
    
#     conn.commit()
#     cur.close()
#     conn.close()

# # 데이터 삭제 함수들
# def delete_user_by_name(name):
#     conn = connect_db()
#     if conn is None:
#         return
    
#     cur = conn.cursor()
    
#     cur.execute('DELETE FROM users WHERE name = %s', (name,))
    
#     conn.commit()
#     cur.close()
#     conn.close()

# def delete_user_by_age(age):
#     conn = connect_db()
#     if conn is None:
#         return
    
#     cur = conn.cursor()
    
#     cur.execute('DELETE FROM users WHERE age = %s', (age,))
    
#     conn.commit()
#     cur.close()
#     conn.close()

# def delete_user_by_id(id):
#     conn = connect_db()
#     if conn is None:
#         return
    
#     cur = conn.cursor()
    
#     cur.execute('DELETE FROM users WHERE id = %s', (id,))
    
#     conn.commit()
#     cur.close()
#     conn.close()

# # 사용 예시
# if __name__ == "__main__":
#     # 테이블 생성
#     create_table()
    
#     # 데이터 삽입
#     insert_user("홍길동", 25)
#     insert_user("김철수", 30)
    
#     # 데이터 조회
#     users = get_users()
#     print("모든 사용자:", users)
    
#     # 특정 사용자 조회
#     user = get_user_by_name("홍길동")
#     print("홍길동:", user)
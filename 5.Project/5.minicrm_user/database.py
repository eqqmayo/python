import sqlite3

DATABASE = 'mycrm.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    # 여기 db로 부터 가져온 내용을 dict 로 하고 싶으면?
    conn.row_factory = sqlite3.Row
    return conn


# 사용자(user) ------------------------------------------------------
def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return [dict(user) for user in users]

def get_users_per_page(page, limit):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users LIMIT ? OFFSET ?', (limit, (page-1) * limit))
    users = cursor.fetchall()
    conn.close()
    return [dict(user) for user in users]

def get_user_count():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM users')
    user_count = cursor.fetchone()[0]
    conn.close()
    return user_count

# 상점(store) ------------------------------------------------------
def get_stores():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stores')
    stores = cursor.fetchall()
    conn.close()
    # 튜플형 데이터를 dict로 변환
    # stores_dict = [{'id': store[0], 'name': store[1], 'type': store[2], 'address': store[3]} for store in stores]
    return [dict(store) for store in stores]

def get_stores_by_name(name: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stores WHERE name Like ?', (f'%{name}%', ))
    stores = cursor.fetchall()
    conn.close()
    return [dict(store) for store in stores]
import sqlite3 

conn = sqlite3.connect("example.db")

cur = conn.cursor() 

# 데이터 삽입
# cur.execute('DELETE FROM users WHERE name="Alice"')
cur.execute('DELETE FROM users WHERE name=?', ('Bob', ))  # 인자 하나만 넣을때는 , 까지 적어줘야 튜플로 인식

conn.commit()

conn.close()


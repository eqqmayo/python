import sqlite3 

conn = sqlite3.connect("example.db")

cur = conn.cursor() 

# 데이터 수정
cur.execute('UPDATE users SET age=10 WHERE name="Alice"')
cur.execute('UPDATE users SET age=? WHERE id=?', (50, 1))

conn.commit()

conn.close()


import sqlite3 

conn = sqlite3.connect("example.db")

cur = conn.cursor() 

# 데이터를 조회한다
cur.execute('SELECT COUNT(*) FROM users')
count = cur.fetchone()[0]

if count == 0:  # 아무 사용자도 없으면 그때 삽입하기
    cur.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Charlie', 22))
else: 
    print('이미 데이터 존재하니 삽입 안함')

conn.commit()

conn.close()


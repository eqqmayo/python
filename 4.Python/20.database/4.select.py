import sqlite3 

conn = sqlite3.connect("example.db")

cur = conn.cursor() 

# 데이터 조회
# cur.execute('SELECT COUNT(*) FROM users')
cur.execute('SELECT * FROM users')

# 결과 가져오기 - 모든 행 가져오기
rows = cur.fetchall()  # COUNT 를 할때는 어차피 하나이기 때문에 fetchone 이 나음
# rows = cur.fetchone()
# rows = cur.fetchone()[0]
print(rows)

conn.commit()

conn.close()


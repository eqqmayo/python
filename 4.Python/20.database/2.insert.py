import sqlite3 

conn = sqlite3.connect("example.db")

cur = conn.cursor() 

# 데이터 삽입
cur.execute('''
    INSERT INTO users (name, age) VALUES ('Alice', 30)
''')

cur.execute('''
    INSERT INTO users (name, age) VALUES ('Bob', 20)
''')

# '?'는 placeholder
# prepared statement 라고 부름. SQL injection 공격을 막는 패턴
cur.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', ('Charlie', 22))

conn.commit()

conn.close()


import sqlite3  # 기본 내장

# DB 연결
conn = sqlite3.connect("example.db")

# 커서 객체 생성
cur = conn.cursor()  # 입출력할 인터페이스를 만들겠다

# 커서를 중심으로 우리 DB에 입출력을 한다
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')

# 변경사항 저장
conn.commit()

# DB 연결 종료
conn.close()


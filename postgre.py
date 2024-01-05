import psycopg2
# envファイルから環境変数を読み込む
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("TESTUSER")
db = os.getenv("TESTDATABASE")
password = os.getenv("TESTPASSWORD")

# PostgreSQLに接続する
conn = psycopg2.connect(
    host="localhost",
    database=db,
    user=user,
    password=password
)
# カーソルを取得する
cur = conn.cursor()

# テーブルを作成する
# cur.execute("""
#     CREATE TABLE users (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(255),
#         email VARCHAR(255)
#     )
# """)
# 作成ずみ

# 保存を実行（忘れると保存されないので注意）
# conn.commit()

# データを挿入する
cur.execute("""
    INSERT INTO users (name, email)
    VALUES (%s, %s)
""", ("Sans", "sans@example.com"))
conn.commit()

# データを抽出する
cur.execute("SELECT * FROM users")

rows = cur.fetchall()

for row in rows:
    print(row)
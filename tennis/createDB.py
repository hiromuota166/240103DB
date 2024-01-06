# testtennisDBのスキーマとテーブルを作成する
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

db = os.getenv("TESTTENNISDB")
user = os.getenv("PCUSER")
password = os.getenv("PCPASSWORD")

# PostgreSQLに接続する
conn = psycopg2.connect(
    host="localhost",
    database=db,
    user=user,
    password=password
)
# カーソルを取得する
cur = conn.cursor()

# スキーマの作成
cur.execute("""
    CREATE SCHEMA IF NOT EXISTS members;
""")
conn.commit() # 保存を実行（忘れると保存されないので注意）

# テーブルを作成する
cur.execute("""
    CREATE TABLE members.player (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        age INTEGER,
        year INTEGER,
        sex VARCHAR(1),
        faculty VARCHAR(50),
        role VARCHAR(50) DEFAULT '部員'
    )
""")
conn.commit()


# メンバーを入れる
import psycopg2
from dotenv import load_dotenv
import os

# 環境変数を読み込む
load_dotenv()

# 環境変数からデータベース接続情報を取得
db = os.getenv("TESTTENNISDB")
user = os.getenv("PCUSER")
password = os.getenv("PCPASSWORD")

try:
    # PostgreSQLに接続
    conn = psycopg2.connect(
        host="localhost",
        database=db,
        user=user,
        password=password
    )
    # カーソルを取得
    cur = conn.cursor()

    # メンバーを挿入するSQLコマンド
    insert_query = """
    INSERT INTO members.player (id, name, age, year, sex, faculty, role)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    player_data = (1, '太田啓夢', 20, 2, 'M', '情報理工', '副会長')

    # SQLコマンドの実行
    cur.execute(insert_query, player_data)

    # 変更をコミット
    conn.commit()

    # リソースのクリーンアップ
    cur.close()
    conn.close()
except Exception as e:
    print(f"An error occurred: {e}")
    if conn:
        conn.rollback()
        cur.close()
        conn.close()

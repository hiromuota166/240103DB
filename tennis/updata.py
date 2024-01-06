import psycopg2
from dotenv import load_dotenv
import os

# 環境変数を読み込む
load_dotenv()

# データベース接続情報を環境変数から取得
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

    # 更新するプレイヤーのID
    player_id = 2

    # プレイヤーの情報を取得
    cur.execute("SELECT * FROM members.player WHERE id = %s;", (player_id,))
    player = cur.fetchone()
    if player is not None:
        # ここでプレイヤーの情報を更新
        updated_name = '田中暖人'
        updated_age = 21

        # データを更新する
        cur.execute("UPDATE members.player SET name = %s, age = %s WHERE id = %s;",
                    (updated_name, updated_age, player_id))
        conn.commit()
    else:
        print(f"No player found with id {player_id}")

    # リソースのクリーンアップ
    cur.close()
    conn.close()
except Exception as e:
    print(f"An error occurred: {e}")
    if conn:
        conn.rollback()
        cur.close()
        conn.close()

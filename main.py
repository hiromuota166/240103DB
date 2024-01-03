import sqlite3

dbname = 'trains.db'

conn=sqlite3.connect(dbname)
c = conn.cursor()

# executeメソッドでSQL文を実行する
create_table = 'create table tennis (id value,name verchar)'
c.execute(create_table)

# SQL文に値をセットする場合は，Pythonのformatメソッドなどは使わずに，
# セットしたい場所に?を記述し，executeメソッドの第2引数に?に当てはめる値をタプルで渡す．
sql = 'insert into tennis (id, name) values (?,?)'
namelist = (26002200600, "太田啓夢")
c.execute(sql, namelist)

conn.commit()

select_sql = 'select * from tennis'

c.execute(select_sql)
result=c.fetchone()

conn.close()

print(result)
import sqlite3
from test_alice_base import Tester


tester = Tester()
connection = sqlite3.connect(r'C:\Users\kiril\Documents\Python\хакатон алиса\base2.db')
cursor = connection.cursor()
# cursor.execute("ВАШ-SQL-ЗАПРОС-ЗДЕСЬ;")

cursor.execute("""CREATE TABLE IF NOT EXISTS attractions(  
   attract_id INT PRIMARY KEY,
   attraction TEXT,
   apperience TEXT,
   link TEXT);
""")
connection.commit()


cursor.execute("""CREATE TABLE IF NOT EXISTS users(  
   user_id INT PRIMARY KEY,
   attractioncames INT,
   locations TEXT);
""")
connection.commit()


'''cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
connection.commit() загрузить кортеж user с информацией о чем-то'''

for i in range(30):
    user = tester.test()
    cursor.execute("INSERT INTO users VALUES(?, ?, ?);", user)
    connection.commit()
'''анологично добавить много пользователей'''



cursor.execute("SELECT * FROM users;")
all_results = cursor.fetchall()
a, b = '{', '}'
for i in range(1, 31):
    print(f'{all_results[i][0]}: {a}attraction_cames: {all_results[i][1]}, locations_was: {all_results[i][2]}{b}')
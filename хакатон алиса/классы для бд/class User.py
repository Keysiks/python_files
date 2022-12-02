import sqlite3

connection = sqlite3.connect(r'C:\Users\kiril\Documents\Python\хакатон алиса\base_for_user.db')
cursor = connection.cursor()
# cursor.execute("ВАШ-SQL-ЗАПРОС-ЗДЕСЬ;")

cursor.execute("""CREATE TABLE IF NOT EXISTS users(  
   user_id INT PRIMARY KEY,
   roads TEXT,
   locations TEXT,
   progress INT);
""")
connection.commit()


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def add_user_in_data(self):
        cursor.execute("""INSERT INTO users(userid, roads, locations, progress) 
           VALUES(str(self.user_id), [], [], 0);""")
        connection.commit()

    def add_road_in_data(self):
        pass


for i in range(11111111, 11111130):
    user = User(i)
    user.add_user_in_data()
cursor.execute("SELECT * FROM users;")
a, b = '{', '}'
all_results = cursor.fetchmany()
for i in range(1, len(all_results) + 1):
    print(f'{all_results[i][0]}: {a}roads: {all_results[i][1]}, locations: {all_results[i][2]}, progress: {all_results[i][3]}{b}')
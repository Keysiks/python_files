import sqlite3


class userBD1:

    def __init__(self, path) -> None:
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        # cursor.execute("ВАШ-SQL-ЗАПРОС-ЗДЕСЬ;")

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(  
        user_id TEXT PRIMARY KEY,
        roads_id TEXT,
        road_progress INT);
        """)
        self.connection.commit()

    def add_user_in_data(self, user_id):
        """добавляет по id пользователя его в базу данных создает прогресс 0 и строку с пройдеными дорогами"""
        self.cursor.execute("INSERT INTO users VALUES(?, ?, ?);", (user_id, '', 0))
        self.connection.commit()

    def add_road_in_data_on_user(self, user_id, road_id):
        res = self.cursor.execute(f'SELECT * FROM users WHERE user_id="{str(user_id)}"').fetchone()
        self.cursor.execute(f'DELETE FROM users WHERE user_id="{str(user_id)}"')
        a = str(res[1] + ' ' + str(road_id)).strip()
        self.cursor.execute("INSERT INTO users VALUES(?, ?, ?);", (str(user_id), a, (str(res[2]) + ' ' + '0').strip()))
        self.connection.commit()

    def get_user_info(self, user_id_find):
        """возвращает по id данные пользователя, если такого нет None"""
        res = self.cursor.execute(f"SELECT * FROM users WHERE user_id='{user_id_find}';").fetchone()
        if res is None:
            return None
        self.connection.commit()
        a = {}
        for i in range(len(res[1].split())):
            a[res[1].split()[i]] = res[2].split()[i]
        return a

    def change_user_progress(self, user_id, road_id):
        res = self.cursor.execute(f'SELECT * FROM users WHERE user_id="{str(user_id)}"').fetchone()
        self.cursor.execute(f'DELETE FROM users WHERE user_id="{str(user_id)}"')
        for i in range(len(res[1].split())):
            if res[1].split()[i] == str(road_id):
                a = res[2].split()[i]
                list1 = res[2].split()
                list1[i] = str(int(a) + 1)
        self.cursor.execute("INSERT INTO users VALUES(?, ?, ?);", (str(user_id), res[1], ' '.join(list1)))
        self.connection.commit()

    def reset_road_on_user(self, user_id, road_id):
        res = self.cursor.execute(f'SELECT * FROM users WHERE user_id="{str(user_id)}"').fetchone()
        self.cursor.execute(f'DELETE FROM users WHERE user_id="{str(user_id)}"')
        for i in range(len(res[1].split())):
            if res[1].split()[i] == str(road_id):
                list1 = res[2].split()
                list1[i] = '0'
        self.cursor.execute("INSERT INTO users VALUES(?, ?, ?);", (str(user_id), res[1], ' '.join(list1)))
        self.connection.commit()

    def closeCon(self):
        self.connection.close()


class quizBD1:

    def __init__(self, path) -> None:
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        # cursor.execute("ВАШ-SQL-ЗАПРОС-ЗДЕСЬ;")

    def closeCon(self):
        self.connection.close()

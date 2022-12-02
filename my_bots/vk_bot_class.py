import sqlite3
import random
import datetime as dt


class VkBot:
    def __init__(self, user_id):
        self.skins = ['defolt', 'medium', 'hard']
        self.status = {'Шудр': [[i for i in range(51)], 150], "Вайшай": [[i for i in range(51, 101)], 200],
                       "Кшатр": [[i for i in range(101, 151)], 300], 'Брахман': [[i for i in range(101, 500)], 350]}
        self.zp = {'Шудр': 150, "Вайшай": 200,
                   "Кшатр": 300, 'Брахман': 350}
        self.user_id = user_id
        self.zp_k = 0.9
        self.last_rating_change = dt.date(2022, 4, 4)
        self.last_get_zp = dt.date(2022, 4, 27)
        self.connection = sqlite3.connect('base_for_user.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(  
           user_id TEXT PRIMARY KEY,
           rating INT,
           balance INT,
           skin TEXT,
           status TEXT);
        """)
        self.connection.commit()

    def add_user(self):
        self.cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?);", (self.user_id, 25, 100, 'defolt', 'Шудр'))
        self.connection.commit()

    def get_instructions(self):
        ins = 'в нашем боте есть 4 статуса, каждому статусу соответсвуют 3 скина' \
              'от скина зависит ваша зарплата, скины можно менять сколько угодно, это стоит 50$ ' \
              'от рейтинга зависит ваша зарплата и возможности, рейтинг можно менять один раз в день командой "измени рейтинг", вам будет ' \
              'добавлен рейтинг в диапозоне от -5 до 10' \
              'чтобы получить зарплату напишите "начисли зп", зарплату можно начислять каждые 3 дня' \
              'чтобы изменить скин, напишите "измени скин"' \
              'усли хотите получить информацию о себе напишите "инфа"' \
              'приятной игры!'
        return ins

    def check_user_in_data(self):
        return True if self.cursor.execute(
            f'SELECT * FROM users WHERE user_id={self.user_id}').fetchone() is not None else False

    def change_rating(self):
        a = str(dt.datetime.now().date() - self.last_rating_change)
        if a[0] != '0':
            b = random.randint(-5, 10)
            rat = self.cursor.execute(f'SELECT * FROM users WHERE user_id={self.user_id}').fetchone()[1]
            self.cursor.execute(f"""UPDATE users SET rating = {rat + b} WHERE user_id={self.user_id}""")
            self.last_rating_change = dt.datetime.now().date()
            self.connection.commit()
            return b
        else:
            return False

    def change_skin(self):
        new_skin = self.skins[random.randint(0, 2)]
        res = self.cursor.execute(f'SELECT * FROM users WHERE user_id={self.user_id}').fetchone()
        if res[2] >= 50:
            self.cursor.execute(f"""UPDATE users SET skin = {new_skin} WHERE user_id={self.user_id}""")
            self.cursor.execute(f"""UPDATE users SET balance = {res[2] - 50} WHERE user_id={self.user_id}""")
            self.connection.commit()
            return new_skin
        else:
            return False

    def check_all(self):
        res = self.cursor.execute(f'SELECT * FROM users WHERE user_id={self.user_id}').fetchone()
        for i in self.status.keys():
            if int(res[1]) in self.status[i][0] and i != res[-1]:
                self.cursor.execute(f"""UPDATE users SET status = {i} WHERE user_id={self.user_id}""")
                self.cursor.execute(f"""UPDATE users SET skin = {'defolt'} WHERE user_id={self.user_id}""")
        if res[-2] == self.skins[0]:
            self.zp_k = 0.9
        elif res[-2] == self.skins[1]:
            self.zp_k = 1.2
        else:
            self.zp_k = 1.5
        self.connection.commit()

    def get_zp_koef(self):
        return self.zp_k

    def get_zp(self):
        a = str(dt.datetime.now().date() - self.last_get_zp)
        res = self.cursor.execute(f'SELECT * FROM users WHERE user_id={self.user_id}').fetchone()
        if a[0] != '0':
            self.cursor.execute(
                f"UPDATE users SET balance = {res[2] + self.zp[res[-1]] * self.zp_k} WHERE user_id={self.user_id}")
            self.last_get_zp = dt.datetime.now().date()
            self.connection.commit()
            return True
        else:
            return False

    def get_info(self):
        res = self.cursor.execute(f'SELECT * FROM users WHERE user_id={self.user_id}').fetchone()
        return f'рейтинг: {res[1]} \n' \
               f'баланс: {res[2]} \n' \
               f'скин: {res[3]} \n' \
               f'статус: {res[4]} \n' \
               f'зарплата: {self.zp[res[-1]]}'



import sqlite3

connection = sqlite3.connect('base_for_user.db')
cursor = connection.cursor()
# cursor.execute("ВАШ-SQL-ЗАПРОС-ЗДЕСЬ;")

# cursor.execute("DROP TABLE IF EXISTS users")

cursor.execute("""CREATE TABLE IF NOT EXISTS users(  
   user_id TEXT PRIMARY KEY,
   roads_id TEXT,
   road_progress TEXT,
   is_complited TEXT);
""")
connection.commit()


def add_user_in_data(user_id):
    """добавляет по id пользователя его в базу данных создает прогресс 0 и строку с пройдеными дорогами"""
    cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?);", (str(user_id), '', '', ''))
    connection.commit()


def add_road_in_data_on_user(user_id, road_id):
    res = cursor.execute(f'SELECT * FROM users WHERE user_id={str(user_id)}').fetchone()
    cursor.execute(f'DELETE FROM users WHERE user_id={str(user_id)}')
    a = str(res[1] + ' ' + str(road_id)).strip()
    cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?);", (str(user_id), a, str(res[2] + ' ' + '0').strip(), str(res[3] + ' ' + 'False')))
    connection.commit()


def get_user_info(user_id_find):
    """возвращает по id данные пользователя, если такого нет None"""
    res = cursor.execute(f"SELECT * FROM users WHERE user_id={user_id_find};").fetchone()
    if res == []:
        return None
    connection.commit()
    a = {}
    for i in range(len(res[1].split())):
        a[res[1].split()[i]] = {'progress': res[2].split()[i], 'completed': res[3].split()[i]}
    return a


def change_user_progress(user_id, road_id):
    res = cursor.execute(f'SELECT * FROM users WHERE user_id={str(user_id)}').fetchone()
    cursor.execute(f'DELETE FROM users WHERE user_id={str(user_id)}')
    for i in range(len(res[1].split())):
        if res[1].split()[i] == str(road_id):
            a = res[2].split()[i]
            list1 = res[2].split()
            list1[i] = str(int(a) + 1)
    cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?);", (str(user_id), res[1], ' '.join(list1), res[3]))
    connection.commit()


def reset_road_on_user(user_id, road_id):
    res = cursor.execute(f'SELECT * FROM users WHERE user_id={str(user_id)}').fetchone()
    cursor.execute(f'DELETE FROM users WHERE user_id={str(user_id)}')
    for i in range(len(res[1].split())):
        if res[1].split()[i] == str(road_id):
            list1 = res[2].split()
            list1[i] = '0'
    cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?);", (str(user_id), res[1], ' '.join(list1), res[3]))
    connection.commit()


def change_complited_of_road(user_id, road_id, flag):
    res = cursor.execute(f'SELECT * FROM users WHERE user_id={str(user_id)}').fetchone()
    cursor.execute(f'DELETE FROM users WHERE user_id={str(user_id)}')
    a = res[3].split()
    for i in range(len(res[2].split())):
        if res[1].split()[i] == str(road_id):
            a.insert(i, str(flag))

    cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?);", (str(user_id), res[1], res[2], ' '.join(a)))


add_user_in_data(1111)
add_road_in_data_on_user(1111, 2222)
add_road_in_data_on_user(1111, 2223)
change_user_progress(1111, 2222)
print(get_user_info(1111))
reset_road_on_user(1111, 2222)
change_complited_of_road(1111, 2222, 'True')
print(get_user_info(1111))

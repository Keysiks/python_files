import sqlite3

connection = sqlite3.connect('base_for_attraction.db')
cursor = connection.cursor()
# cursor.execute("ВАШ-SQL-ЗАПРОС-ЗДЕСЬ;")
connection.commit()

# cursor.execute("DROP TABLE IF EXISTS attractions")
cursor.execute("""CREATE TABLE IF NOT EXISTS attractions(  
   place_id TEXT PRIMARY KEY,
   short_desk TEXT,
   photo_url TEXT,
   routes_id TEXT,
   short_desc1 TEXT,
   photo_url1 TEXT);
""")
connection.commit()


def add_place(place_id, short_desk='', photo_url='', routes_id='', text='', photo_url1=''):
    # добавляет полную информацию о месте, можно добавлять место только по id остальную инфу потом дописать
    cursor.execute("INSERT INTO attractions VALUES(?, ?, ?, ?, ?, ?);",
                   (str(place_id), short_desk, photo_url, routes_id, text, photo_url1))
    connection.commit()


def get_info_about_place(place_id_find):
    """возвращает по id данные места, если такого нет None"""
    res = cursor.execute(f"SELECT * FROM attractions WHERE place_id={place_id_find};").fetchone()
    return None if res == [] else {res[0]: {'shortDesc': res[1], 'photo_url': res[2],
                                            'routes': {res[3]: {'shortDesc': res[4], 'photoURL': res[5]}}}}


# вносишь сюда кортеж обязательно в него айди места и инфу которую надо поменять и в кортеж надо вносить всю инфу о пользователе получить ее можно по айди
# функция получчения информации есть
''' place_id TEXT PRIMARY KEY,
   short_desk TEXT,
   photo_url TEXT,
   routes_id TEXT,
   short_desc1 TEXT,
   photo_url1 TEXT переменные в кортеж вписывать в таком порядке'''


def add_info_about_somethihg(change_some):
    cursor.execute(f"DELETE FROM attractions WHERE place_id={str(change_some[0])};")
    cursor.execute("INSERT INTO attractions VALUES(?, ?, ?, ?, ?, ?);",
                   (str(change_some[0]), change_some[1], change_some[2], str(change_some[3]), change_some[4], change_some[5]))
    connection.commit()


some = (1111, 'blabla', 'url.py', 1212, 'bla1', 'url1')
for i in range(1111, 1120):
    add_place(i, 'blabla', 'url.py', '1211', 'bla1', 'url1')
for i in range(1111, 1120):
    print(get_info_about_place(i))
add_info_about_somethihg(some)
print()
print(get_info_about_place('1111'))
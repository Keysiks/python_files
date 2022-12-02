# Импортируем библиотеку vk_api
import vk_api
# Достаём из неё longpoll
from vk_api.longpoll import VkLongPoll, VkEventType
import sqlite3
import random

# Создаём переменную для удобства в которой хранится наш токен от группы

token = "fec0feb2b7b3d278fef15af3844e42b607683415a814a0210ad0e7e0105793046661b34dc18ecb004b2eb"

# Подключаем токен и longpoll
bh = vk_api.VkApi(token=token)
give = bh.get_api()
longpoll = VkLongPoll(bh)

connection = sqlite3.connect('base_for_pivo2.db')
cursor = connection.cursor()
# cursor.execute("ВАШ-SQL-ЗАПРОС-ЗДЕСЬ;")

cursor.execute("DROP TABLE IF EXISTS users")

cursor.execute("""CREATE TABLE IF NOT EXISTS users(  
   user_id TEXT PRIMARY KEY,
   name TEXT,
   rating INT,
   balance INT,
   zarp INT);
""")
connection.commit()
users = ['Никита Шаронов', 'Андрей Пижонков', "Алексей Щукин", "Евгений Паличев", "Редько Кирилл", "Тамир Козлов",
         "Максим Спиркин", "Дарья Сысуева", "Артем Безруков", "Ильнур Патеев", "Даниил Дуничев", "Илья Тыкушин",
         "Николай Новиков", "Эмиль Валиуллов", "Максим Паньженский", "Паша Северьянов", "Александр Казаков",
         "Руслан Гильфанов", "Лисовол Владимир"]


# Создадим функцию для ответа на сообщения в лс группы
def send_msg(id, text):
    bh.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


# 756489 код админки
admin = False
reg = False
name = ''
admins = []
# Слушаем longpoll(Сообщения)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            if request == "/start":
                send_msg(event.user_id, 'Представьтесь в данной форме: "Имя: имя фамилия"')
            elif request.split()[0].lower() == 'имя:':
                name = request.split()[1] + ' ' + request.split()[2]
                if name in users:
                    send_msg(event.user_id, f'Здраствуйте, вы уже в партии')
                    reg = True
                else:
                    send_msg(event.user_id, "Введите код партии")
            elif request == '1752':
                if reg is not True:
                    send_msg(event.user_id, 'Вы в партии!')
                    cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?);",
                                   (str(event.user_id), name, 10, 10000, 1000000))
                    connection.commit()
                    reg = True
                    users.append(name)
            elif request == '756489':
                send_msg(event.user_id, 'Вы стали админом!')
                res = cursor.execute(f"SELECT * FROM users WHERE user_id={event.user_id}").fetchone()
                admins.append(res[1])
                admin = True
            elif request.lower() == 'как работает' or request.lower() == "инструкции" or request.lower() == "применение":
                send_msg(event.user_id,
                         'Представьтесь в данной форме: "Имя: имя фамилия", затем можете ввести код админа, если знаете его, иначе вы будете зарегестрирован как участник')
            elif request.lower() == 'информация обо мне' or request.lower() == 'инфа обо мне':
                if reg is True:
                    res = cursor.execute(f"SELECT * FROM users WHERE user_id={event.user_id}").fetchone()
                    send_msg(event.user_id,
                             f'name: {res[1]} \nrating: {res[2]} \nbalance: {res[3]} \n zarplata: {res[4]}')
                else:
                    send_msg(event.user_id, 'Сначала зарегестрируйтесь, если не знаете как, напишите "как работает"')
            elif request.lower() == 'курс' or request.lower() == 'курс валют':
                send_msg(event.user_id, f'1€ = 78Р \n1$ = 73Р \n1биткоин = 3000069Р')
            elif 'соц' in request.lower():
                send_msg(event.user_id,
                         'если хотите изменить рейтинг пользователю напишите: "+ имя и фамилия члена партии" этому человеку прибавится или убавится рейтинг')
            elif '+' in request:
                a = random.randint(-10, 20)
                # написать рфинд от + + 1
                if request[request.rfind('+') + 1:] in users:
                    res = cursor.execute(f'SELECT * FROM users WHERE name={name}').fetchone()
                    send_msg(event.user_id, 'работает')
                    cursor.execute(f'DELETE FROM users WHERE name={name}')
                    cursor.execute(f'INSERT INTO users VALUES(?, ?, ?, ?, ?);',
                                   (str(event.user_id), res[1], res[2] + a, res[3], res[4]))
                    send_msg(event.user_id, f'Принято, рейтинг данного человека измнен на {a}')
            else:
                send_msg(event.user_id, 'напишите "как работает"')

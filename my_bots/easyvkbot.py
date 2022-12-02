# Импортируем библиотеку vk_api
import vk_api
# Достаём из неё longpoll
from vk_api.longpoll import VkLongPoll, VkEventType

# Создаём переменную для удобства в которой хранится наш токен от группы

token = "fec0feb2b7b3d278fef15af3844e42b607683415a814a0210ad0e7e0105793046661b34dc18ecb004b2eb"

# Подключаем токен и longpoll
bh = vk_api.VkApi(token=token)
give = bh.get_api()
longpoll = VkLongPoll(bh)


# Создадим функцию для ответа на сообщения в лс группы
def send_msg(id, text):
    bh.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


admin = False
reg = False
users = {}
admins = {}
# Слушаем longpoll(Сообщения)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            if request == "/start":
                send_msg(event.user_id, 'Представьтесь в данной форме: "Имя: Ваше имя"')
            elif request.split()[0].lower() == 'имя:':
                if request.split()[1].lower() in users.keys():
                    send_msg(event.user_id, f'Здраствуйте, вы уже в партии')
                else:
                    send_msg(event.user_id, 'Вы добавлены в партию')
                    users[event.user_id] = {'name': request.split()[1].lower(), 'rating': 100, 'balance': 0,
                                            'role': 'user'}
                    reg = True
            elif request == '1752':
                send_msg(event.user_id, 'Админ, представьтесь в данной форме: "Админ: ваше имя"')
                admin = True
            elif request.split()[0].lower() == 'админ':
                if admin is True:
                    if request.split()[1].lower() in admins.keys():
                        send_msg(event.user_id, 'Здраствуйте глубокоуважаемый админ')
                    else:
                        send_msg(event.user_id, "Вы добавлены в список админов")
                        admins[event.user_id] = {'name': request.split()[1].lower(), 'rating': 100, 'balance': 0,
                                                 'role': 'admin'}
                else:
                    send_msg(event.user_id, 'Вы удалены из партии за попытку вранья')
            elif request.lower() == 'как работает' or request.lower() == "инструкции" or request.lower() == "применение":
                send_msg(event.user_id,
                         'Представьтесь в данной форме: "Имя: Ваше имя", затем можете ввести код админа, если знаете его, иначе вы будете зарегестрирован как участник')
            elif request.lower() == 'информация обо мне' or request.lower() == 'инфа обо мне':
                if reg is True:
                    a = users[event.user_id]
                    send_msg(event.user_id, f'rating: {a["rating"]} \nbalance: {a["balance"]} \nrole {a["role"]}')
                else:
                    send_msg(event.user_id, 'Сначала зарегестрируйтесь, если не знаете как, напишите "как работает"')
            else:
                send_msg(event.user_id, 'напишите "как работает"')

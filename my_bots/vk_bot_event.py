from vk_bot_class import VkBot
# изменить функцию изменения скина, хреново работает

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

token = "fec0feb2b7b3d278fef15af3844e42b607683415a814a0210ad0e7e0105793046661b34dc18ecb004b2eb"

bh = vk_api.VkApi(token=token)
give = bh.get_api()
longpoll = VkLongPoll(bh)


def send_msg(id, text):
    bh.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text.lower()
            id = event.user_id
            if message == '/start':
                vk = VkBot(id)
                if vk.check_user_in_data():
                    send_msg(id, 'Привет, вы уже зарегестрированы')
                else:
                    send_msg(id, 'Привет, зарегистрируйтесь командой /reg')

            elif 'инструкции' in message or 'как работает' in message or 'помощь' in message:
                send_msg(id, vk.get_instructions())
            elif '/reg' in message:
                if vk.check_user_in_data():
                    send_msg(id, 'Bы уже зарегестрированы')
                else:
                    send_msg(id, 'Вы зарегистрированы')
                    vk.add_user()
            elif 'инфа' in message:
                if vk.check_user_in_data():
                    res = vk.get_info()
                    send_msg(id, res)
                else: send_msg(id, 'сначала зарегиструйтесь командой /reg')
            elif 'начисли зп' in message:
                res = vk.get_zp()
                if res:
                    send_msg(id, 'Зарплата начислена')
                else:
                    send_msg(id, "Подождите до следующего начисления зарплаты")
            elif 'измени скин' in message:
                res = vk.change_skin()
                if res is False:
                    send_msg(id, 'У вас не хваатет денег, чтобы изменить скин, наберите 50$')
                else:
                    send_msg(id, f'Ваш скин изменен на {res}')
                vk.check_all()
            elif 'измени рейтинг' in message:
                res = vk.change_rating()
                if res is False:
                    send_msg(id, f'Ваш рейтинг не изменен, вы уже меняли рейтинг сегодня')
                else:
                    send_msg(id, f'Ваш рейтинг изменен на {res}')
            elif 'бб' in message or 'пока' in message:
                send_msg(id, 'Мне будет без тебя скучно( Возвращайся снова😉')
            else:
                send_msg(id, 'Извините, непонятно. Напишите "как работает"')
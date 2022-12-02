import telebot
from telebot import types
from telebot_class1 import Telebotgamer

bot = telebot.TeleBot('5379467568:AAHoZywKumutv5PvQrqG-zYXGALOJ5aHDSs')
tb = Telebotgamer()


@bot.message_handler(content_types=['text', 'audio', 'document', 'jpg', 'jpeg'])
def get_text_messages(message):
    global tb
    id = message.from_user.id
    mess = message.text.lower()
    if mess == "привет" or mess == '/start':
        bot.send_message(id, "Привет, выбери что-нибудь")
        keyboard_scope(message)
    elif mess == "меню" or mess == 'в меню':
        keyboard_scope(message)
    elif mess == '/help' or mess == 'помощь':
        bot.send_message(id, 'Напишите "Привет"')
    elif 'больше' in mess or 'меньше' in mess or 'равно' in mess:
        res = tb.game_num_100(mess)
        if res is True:
            bot.send_message(id, 'Да')
        elif res is False:
            bot.send_message(id, 'Нет')
        elif res == 'lost':
            bot.send_message(id, 'К сожалению вы проиграли(')
        elif res == 'win':
            bot.send_message(id, 'Поздравляем с победой!')
        elif res == 'game_end':
            bot.send_message(id, 'Игра окончена, чтобы начать новую игру напишите "Новая игра"')
    elif 'новая игра' in mess:
        tb.change_running()
        keyboard_game(message)
    elif mess == 'выход':
        quit()
    else:
        bot.send_message(id, 'Извините, непонятно')


def keyboard_scope(message):
    keyboard = types.InlineKeyboardMarkup()
    key_music = types.InlineKeyboardButton(text='Лучшая музыка', callback_data='Music')
    keyboard.add(key_music)
    key_memas = types.InlineKeyboardButton(text='Классные мемы', callback_data='Memas')
    keyboard.add(key_memas)
    key_games = types.InlineKeyboardButton(text='Поиграть в игры', callback_data='Games')
    keyboard.add(key_games)
    question = 'Выбери что-нибудь из моих умений:'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_work(call):
    global tb
    player = 0
    diller = 0
    if call.data == 'Games':
        keyboard_game(call)
    elif call.data == 'Memas':
        file = open(tb.get_memas(), 'rb')
        bot.send_photo(call.from_user.id, file)
        button = types.InlineKeyboardMarkup()
        button.add(types.InlineKeyboardButton(text="Продалжаем?", callback_data=f'next_mem'))
        button.add(types.InlineKeyboardButton(text="Меню", callback_data=f'head_menu'))
        bot.send_message(call.from_user.id, text='Продалжаем?', reply_markup=button)
    elif call.data == 'Music':
        pass
    elif call.data == 'game1':
        bot.send_message(call.from_user.id, 'Вы выбрали игру "угадай число от 1 до 100 за 7 ходов". Правила предельно '
                                            'простые: вы вводите сообщение в формате "больше либо меньше здесь ваше '
                                            'число", если хотите проверить равно ли загаданное число, которое вы назвали'
                                            ' напишите "равно ваше число"')
    elif call.data == 'game3':
        bot.send_message(call.from_user.id, 'Вы выбрали игру страна-столица. Я буду вам называть страну, а вы мне '
                                            'должны ответить на предоставлленой клавиатуре выбора')
        country_capital_game_keyboard(call)
    elif 'answer' in call.data:
        if call.data.split('_')[2] == tb.get_capitals_answer():
            bot.send_message(call.from_user.id, 'Правильно!')
            country_capital_game_keyboard(call)
        else:
            bot.send_message(call.from_user.id, 'К сожалению, вы ошиблись')
            country_capital_game_keyboard(call)
    elif call.data == 'next_mem':
        file = open(tb.get_memas(), 'rb')
        bot.send_photo(call.from_user.id, file)
        button = types.InlineKeyboardMarkup()
        button.add(types.InlineKeyboardButton(text="Продалжаем?", callback_data=f'next_mem'))
        button.add(types.InlineKeyboardButton(text="Меню", callback_data=f'head_menu'))
        bot.send_message(call.from_user.id, text='Продалжаем?', reply_markup=button)
    elif call.data == 'head_menu':
        keyboard_scope(call)
    elif call.data == "game2":
        diller = tb.black_jak_game_beginning()
        player = tb.black_jak_game_beginning()
        button = types.InlineKeyboardMarkup()
        button.add(types.InlineKeyboardButton(text="Беру", callback_data="next_card"))
        button.add(types.InlineKeyboardButton(text="Хватит", callback_data="stop_card"))
        bot.send_message(call.from_user.id, text=f"Ваш счет {sum(player)}", reply_markup=button)
    elif call.data == "next_card":
        player.append(tb.black_jak_card())
        button = types.InlineKeyboardMarkup()
        button.add(types.InlineKeyboardButton(text="Беру", callback_data="next_card"))
        button.add(types.InlineKeyboardButton(text="Хватит", callback_data="stop_card"))
        bot.send_message(call.from_user.id, text=f"Ваш счет {sum(player)}", reply_markup=button)




def keyboard_game(message):
    keyboard = types.InlineKeyboardMarkup()
    for i in range(len(tb.get_games())):
        key = types.InlineKeyboardButton(text=tb.get_games()[i], callback_data=f'game{i + 1}')
        keyboard.add(key)
    question = 'Выбирай любую игру!'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


def country_capital_game_keyboard(message):
    global tb
    keyboard = types.InlineKeyboardMarkup()
    res = tb.game_country_capital_desk()
    for i in range(len(res[0])):
        key = types.InlineKeyboardButton(text=res[0][i], callback_data=f'answer_capital_{res[0][i]}')
        keyboard.add(key)
    question = res[1]
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


bot.polling(none_stop=True, interval=0)

import telebot
from telebot import types
import config

bot = telebot.TeleBot('5279553643:AAFvOEfAMjRll1yeAw6Vij1rrihnNCEdjoY')

name = ''


@bot.message_handler(content_types=['text', 'audio', 'document', 'jpg', 'jpeg'])
def get_text_messages(message):
    if message.text == "Привет" or message.text == '/start':
        bot.send_message(message.from_user.id, "Привет, напиши /help, если хочешь узнать мои возможности")
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    elif message.text == '/help':
        bot.send_message(message.from_user.id,
                         "Сначала зарегестрируйтесь командой /reg,если зарегестрировались, то спросите, что я умею")
    elif message.text == 'Что ты умеешь?' or message.text == 'что ты умеешь?':
        bot.send_message(message.from_user.id, f'Вот список моих команд:')
        keyboard1(message)

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


def keyboard1(message):
    keyboard = types.InlineKeyboardMarkup()
    key_music = types.InlineKeyboardButton(text='Лучшая музыка', callback_data='Music')
    keyboard.add(key_music)
    key_memas = types.InlineKeyboardButton(text='Класный мем', callback_data='Memas')
    keyboard.add(key_memas)
    question = 'Выбери что-нибудь из моих умений:'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Отличное имя! Спросите что я умею')


def bot_comands():
    comands = ['Скинуть мем', 'Скинуть список топ 5 треков русской музыки на сегодня']
    return '\n'.join(comands)


def best_music():
    music = ['Малиновая лада', "Солнце Монако", "Я как Федерико Фелини"]
    return music


def get_mem():
    pass


@bot.callback_query_handler(func=lambda call: True)
def callback_work(call):
    if call.data == 'Music':
        list1 = '\n'.join(best_music())
        bot.send_message(call.from_user.id, f"Вот список: \n {list1}")
    elif call.data == 'Memas':
        bot.send_photo(call.from_user.id, open('C:\Users\kiril\Documents\Python\my_bots\мем2.jpeg', 'rb'))


# bot.send_photo(call.message.chat.id, open('C:\Users\kiril\Documents\Python\my_bots\мем2.jpeg'))


bot.polling(none_stop=True, interval=0)

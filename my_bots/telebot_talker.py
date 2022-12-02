import telebot
from telebot import types
import random

bot = telebot.TeleBot('token')

hello = False
theme = ''
talking = False
game = True


@bot.message_handler(content_types=['text', 'audio', 'document', 'jpg', 'jpeg'])
def get_text_messages(messages):
    global hello, theme
    id = messages.from_user.id
    message = messages.text.lower()
    if message == "привет" or message == '/start':
        bot.send_message(id, "Привет, я умный бот) Поболтаем?")
        hello = True
    elif (message == 'да' or message == 'давай' or message == 'погнали') and hello is True:
        bot.send_message(id, 'На какую тему будем болтать?')
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        key_about_life = types.InlineKeyboardButton(text='о жизни)', callback_data='about_life')
        keyboard.add(key_about_life)
        key_tall_something = types.InlineKeyboardButton(text='Расскажи что-нибудь', callback_data='talking')
        keyboard.add(key_tall_something)
        key_play_game = types.InlineKeyboardButton(text='Сыграем в игру', callback_data='game')
        keyboard.add(key_play_game)
        bot.send_message(messages.from_user.id, text='Выберите из предложенных:', reply_markup=keyboard)
    else:
        bot.send_message(id, 'Извините, непонятно')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global theme, talking
    if call.data == "about_life":
        theme = 'О жизни'
        bot.send_message(call.message.chat.id, 'Секунду...')
    elif call.data == "talking":
        theme = 'Рассказать о чем-нибудь'
        talking = True
        bot.send_message(call.message.chat.id, 'Секунду...')
    elif call.data == 'game':
        pass


def game_nums(id):
    global game
    if game is True:
        bot.send_message(id,
                         'Суть игры в том, что я загадываю число от 1 до 100. Тебе же надо его угадать за 6 ходов, '
                         'вопросами, на котрые я могу отвечать да либо нет. Например, "Число больше 50" мой ответ: "да"')
        num = random.randint(1, 100)
        


bot.polling(none_stop=True, interval=0)

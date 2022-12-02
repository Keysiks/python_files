import telebot_talker

bot = telebot.TeleBot('5279553643:AAFvOEfAMjRll1yeAw6Vij1rrihnNCEdjoY')

name = ''


@bot.message_handler(content_types=['text', 'audio', 'document', 'jpg', 'jpeg'])
def get_text_messages(message):
    if message.text == "Привет" or message.text == '/start':
        bot.send_message(message.from_user.id, "Привет, как мне к тебе обращаться?")
    elif message.text == 'Что ты умеешь?' or message.text == "что ты умеешь?":
        bot.send_message(message.from_user.id, f'Вот что я умею: \n {bot_comands()}')
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


def bot_comands():
    comands = ['Скинуть мем', 'Скинуть список топ 5 треков русской музыки на сегодня']
    return '\n'.join(comands)


bot.polling(none_stop=True, interval=0)
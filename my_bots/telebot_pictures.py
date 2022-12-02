import telebot_talker
from telebot_talker import types
import config
import urllib.request
from class_pictures import Fotoshop

bot = telebot.TeleBot('5381678956:AAGckQ1yg763qCELBzhvK3Bia3xdjIVKCOI')


@bot.message_handler(content_types=["document"])
def handle_docs_audio(message):
    document_id = message.document.file_id
    file_info = bot.get_file(document_id)
    urllib.request.urlretrieve(f'http://api.telegram.org/file/bot{config.token}/{file_info.file_path}',
                               file_info.file_path)


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_message(message):
    foto = Fotoshop()
    id = message.from_user.id
    if message == '/start':
        bot.send_message(id, 'Привет, напиши "/инструкции" если хотите узнать как работает бот')
    elif message == 'измени время года':
        foto.change_year_time()


bot.polling(none_stop=True, interval=0)

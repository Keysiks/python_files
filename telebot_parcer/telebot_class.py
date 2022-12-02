import logging
from aiogram import Bot, Dispatcher, executor, types
from bot_token import token

bot = Bot(token=token())
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    await message.reply("Привет, я парсер цен на лего, пиши /help, чтобы узнать мои возможности.")


@dp.message_handler(commands="help")
async def cmd_test1(message: types.Message):
    await message.reply(
        "Я смотрю цены на интересующие вас лего наборы каждый час, если появляется выгодное предложение,"
        "я присылаю Вам уведомление. Напиши /list")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)

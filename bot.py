TOKEN = "5270401029:AAFLMs1JjXXN9QhzRj6A2gXCO1c7jlNiP_0"

from aiogram import Bot, Dispatcher, executor, types
import logging
from aiogram.types import ContentType, File, Message
from main import start_audio
import os

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def register(message: types.Message):
    await bot.send_message(message.from_user.id, "Aссалому алеком")

@dp.message_handler(content_types=[ContentType.TEXT])
async def other_message(message: types.Message):
    if message.text:
        await bot.send_message(message.from_user.id, "Voice yuboring")


@dp.message_handler(content_types=[ContentType.VOICE])
async def other_message(message: types.Message):
    # file_id = message.voice.file_id
    # file = await bot.get_file(file_id)
    # file_path = file.file_path
    # await bot.send_audio(message.from_user.id, result_mp3, performer = "Performer", title = "Title")
    # await bot.download_file(file_path, "voice\\123.mp3")
    voic = os.listdir('voice\\')
    print(voic[0])

    result_mp3 = start_audio(f"voice\\{voic[0]}")
    print(result_mp3)
    # await bot.send_audio(message.from_user.id, result_mp3, performer="Performer", title="Title")




while True:
    try:
        if __name__ == '__main__':
            executor.start_polling(dp, skip_updates=True)
    except:
        continue
    break
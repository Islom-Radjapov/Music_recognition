from aiogram import Bot, Dispatcher, executor, types
import logging
from aiogram.types import ContentType, File, Message
import os
import time
from sql_code import Database
db = Database('database.db')

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
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, "voice\\voice.ogg")

    await bot.send_message(message.from_user.id, "Yuklanmoqda")

    os.system("python main.py")

    music = os.listdir(r"Download_data")

    print(music)
    if music:
        print('Succes BOT')
        file_music = open(fr"Download_data\{music[0]}", 'rb')
        await bot.send_audio(message.from_user.id, file_music, title=music[0])
        file_music.close()
        os.remove(fr"Download_data\{music[0]}")
        text = db.get_text()

        lengh = len(text[0][0])
        try:
            await bot.send_message(message.from_user.id, text[0][0])
        except:
            await bot.send_document(message.from_user.id, text[0][0][:int(lengh / 2)])
            await bot.send_document(message.from_user.id, text[0][0][int(lengh / 2):])
    else:
        await bot.send_message(message.from_user.id, "Qoshiq topilmadi")





while True:
    try:
        if __name__ == '__main__':
            executor.start_polling(dp, skip_updates=True)
    except:
        continue
    break
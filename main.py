from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType, Message
from converter import converter_audio
from configuration import logger, TG_CHANNEL_ID, TG_BOT_TOKEN

bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=[ContentType.VOICE])
async def voice_message_handler(message: Message):
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, file_id)
    await message.reply(converter_audio(file_id))


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет! Я FoxSpeakBot, конвертирую аудиосообщения в текст!\nОтправьте мне аудио для проверки.")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Для начала работы, добавьте меня в чат канала и дайте права администратора. Бот будет писать текст в комментариях сообщения.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)






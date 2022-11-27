from aiogram import Bot, Dispatcher, executor
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
    filename = f"{file_id}.ogg"
    await bot.download_file(file_path, filename)
    await message.reply(converter_audio(filename))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)






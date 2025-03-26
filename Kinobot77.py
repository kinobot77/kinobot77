import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "SIZNING_BOT_TOKENINGIZ"
CHANNEL_ID = -1002332580178  # Kanal ID

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.channel_post_handler()
async def delete_post(message: types.Message):
    await bot.delete_message(chat_id=CHANNEL_ID, message_id=message.message_id)
    print(f"Post o‘chirildi: {message.message_id}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

from aiogram import Bot, Dispatcher, executor, types
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer("🩸 OTAXON MAFIA ishga tushdi.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

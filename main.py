from aiogram import Bot, Dispatcher, executor, types
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

users = {}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    uid = message.from_user.id
    if uid not in users:
        users[uid] = {"olmos": 100}
    await message.answer(
        "🔥 *OTAXON MAFIA BOT*\n\n"
        "💎 Boshlang‘ich olmos: 100\n"
        "📜 Buyruqlar:\n"
        "/balance — olmos\n"
        "/rollar — qorong‘u rollar",
        parse_mode="Markdown"
    )

@dp.message_handler(commands=['balance'])
async def balance(message: types.Message):
    uid = message.from_user.id
    olmos = users.get(uid, {}).get("olmos", 0)
    await message.answer(f"💎 Senda: {olmos} olmos")

@dp.message_handler(commands=['rollar'])
async def rollar(message: types.Message):
    await message.answer(
        "🩸 *QORONG‘U ROLLAR RO‘YXATI*\n\n"
        "👁 Qonli Don\n"
        "🩸 So‘yuvchi\n"
        "☠️ Soya Qotil\n"
        "🧪 Tungi Ruh\n"
        "⚔️ Qora Hakim\n"
        "🧿 Jallod Shifokor",
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

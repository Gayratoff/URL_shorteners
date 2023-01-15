import pyshorteners as sh
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import CommandStart,CommandHelp,Text
from aiogram.utils import executor

TOKEN = "BOT TOKENI JOYLANADI"
# @KINGSOFPY MANBA 
bot=Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(CommandStart())
async def MistrUz(message: types.Message):
    await message.reply("Salom Menga Biron bir URL Yuboring")

@dp.message_handler(Text(startswith="https"))
async def Help(message: types.Message):
    s = sh.Shortener()
    URL = s.tinyurl.short(message.text)
    await message.answer(f"{URL}\n\n Qisqa URL Tayor",disable_web_page_preview=True)


if __name__ =="__main__":
    executor.start_polling(dp)
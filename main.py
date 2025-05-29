import asyncio
import random
from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

TOKEN = "7635546026:AAHr6NBqdrvuyKp8b_wkADGueWnjQClMawY" # @MotivationPicture_bot

IMAGES = [
    "https://i.pinimg.com/736x/44/0d/55/440d55ba625f0b6abd999858f8ac7dfe.jpg",
    "https://i.pinimg.com/736x/61/78/83/61788324415d6dcb9bb3dbbee096e108.jpg",
    "https://i.pinimg.com/736x/5b/63/df/5b63df75c9e36b134f36fe0a29ea203b.jpg",
    "https://i.pinimg.com/736x/fb/ff/8d/fbff8d3e170d2706ce75e1d50aa7b21b.jpg",
    "https://i.pinimg.com/736x/5d/55/67/5d55673187edb98ee11b4d183c1c5f9b.jpg"
]

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

@dp.message(F.text == "/start")
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[[types.InlineKeyboardButton(text="Нажать для мотивации", callback_data="go")]]
    )
    await message.answer("Нажми кнопку и получи мотивацию!", reply_markup=kb)

@dp.callback_query(F.data == "go")
async def motivate(callback: types.CallbackQuery):
    await callback.message.answer_photo(random.choice(IMAGES), caption="Вот твоя мотивация!")
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
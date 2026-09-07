from aiogram.filters import Command
from aiogram import Router, types

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Hello, world!")
    
@router.message()
async def echo_test(message: types.Message):
    print(f"Сообщение полуено: {message.text}")
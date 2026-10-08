import pytz
from aiogram.filters import Command
from aiogram import Router, types
from database.models import User

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user, created = User.get_or_create(
        tg_id = user_id,
        defaults={
            'username': message.from_user.username
        }
    )
    await message.answer("Определите свой часовой пояс(+3):")

@router.message()
async def echo(message: types.Message):
    # ! ->
    timezone = pytz.timezone(message.text)
    User.update(time_zone=timezone).where(User.tg_id == message.from_user.id).execute()
    print("Success")



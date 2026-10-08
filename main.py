import asyncio
from aiogram import Bot, Dispatcher
from config import Config
from handlers.user import router
from database.models import init_db


async def main():
    init_db()
    bot = Bot(token=Config.TOKEN)
    dp = Dispatcher()
    dp.include_router(router=router)
    await dp.start_polling(bot)
    


if __name__ == "__main__":
    asyncio.run(main())

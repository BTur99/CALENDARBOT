import asyncio
from aiogram import Bot, Dispatcher
from config import Config
from handlers.user import router

bot = Bot(token=Config.TOKEN)
dp = Dispatcher()

dp.include_router(router=router)
print("Poyter online", router)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

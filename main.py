import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
import os
# from config import TOKEN

from app.handlers import router
from app.motivation_timer import send_motivation_every_day

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

async def main():
    dp.include_router(router)

    asyncio.create_task(send_motivation_every_day(bot))

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
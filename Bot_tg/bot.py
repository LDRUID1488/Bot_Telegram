import config
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(massage: types.Message):
    await message_answer(massage.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
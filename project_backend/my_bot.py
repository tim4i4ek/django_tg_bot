import os
import django
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from asgiref.sync import sync_to_async


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_settings.settings')
django.setup()


from my_bot.models import Service


TOKEN = "8733279636:AAFhZ3sQ26IBUtZYyUidiEZLUEpE-aChQlo"
bot = Bot(token=TOKEN)
dp = Dispatcher()



@sync_to_async
def get_all_services():
    return list(Service.objects.all())




@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Привіт! Я твій бот для запису. 🏍️\n"
        "Напиши /services, щоб побачити, що ми вміємо!"
    )


@dp.message(Command("services"))
async def show_services(message: types.Message):
    services = await get_all_services()

    if not services:
        await message.answer("У базі поки немає послуг. Додай їх через адмінку Django!")
        return

    response = "Наші послуги:\n\n"
    for s in services:
        response += f"🔹 {s.name} — {s.price} грн\n"

    await message.answer(response)


@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Ти сказав: {message.text}. Але краще натисни /services!")


async def main():
    print("🚀 Бот запущений і підключений до Django!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
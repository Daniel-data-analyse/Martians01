from aiogram import Bot, Dispatcher, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging
import asyncio

API_TOKEN = "7519093340:AAEChSqRMq1ovPju5fGpuLYYYAdSHjmPCVc"

logging.basicConfig(level=logging.INFO)
  
bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Создаем диспетчер

button1 = KeyboardButton(text="1) Регистрация/Изменить профиль")
button2 = KeyboardButton(text="2) Увидеть других")
button3 = KeyboardButton(text="3) Удалить профиль")

main_menu = ReplyKeyboardMarkup(keyboard=[[button1], [button2], [button3]], resize_keyboard=True)

users = {}
names_surnames = set()

async def start_handler(message):
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=main_menu)

dp.message.register(start_handler, F.command("start"))

@dp.message(F.text == "1) Регистрация/Изменить профиль")
async def registration_handler(message):
    user_id = message.from_user.id
    if user_id in users:
        await message.answer("Вы уже зарегистрированы. Хотите изменить профиль? Напишите 'Да' или 'Нет'.")
    else:
        await message.answer("Давайте зарегистрируем вас. Напишите ваше имя:")
        users[user_id] = {"step": "name"}

@dp.message(lambda message: message.from_user.id in users and "step" in users[message.from_user.id])
async def collect_data(message):
    user_id = message.from_user.id
    step = users[user_id].get("step")

    if step == "name":
        if message.text in names_surnames:
            await message.answer("Это имя уже занято, пожалуйста, выберите другое.")
            return
        users[user_id]["Имя"] = message.text
        users[user_id]["step"] = "surname"
        await message.answer("Введите вашу фамилию:")
    elif step == "surname":
        name_surname = f"{users[user_id]['Имя']} {message.text}"
        if name_surname in names_surnames:
            await message.answer("Это имя и фамилия уже заняты, пожалуйста, выберите другие.")
            return
        users[user_id]["Фамилия"] = message.text
        names_surnames.add(name_surname)
        users[user_id]["step"] = "birthdate"
        await message.answer("Введите вашу дату рождения (дд.мм.гггг):")
    elif step == "birthdate":
        users[user_id]["Дата рождения"] = message.text
        users[user_id]["step"] = "gender"
        await message.answer("Введите ваш пол (М/Ж):")
    elif step == "gender":
        gender = message.text.lower()
        if gender in ["м", "ж"]:
            users[user_id]["Пол"] = "Мужской" if gender == "м" else "Женский"
            users[user_id]["step"] = "flowers"
            await message.answer("Введите ваши любимые цветы:")
        else:
            await message.answer("Пожалуйста, введите 'М' или 'Ж'.")
    elif step == "flowers":
        users[user_id]["Любимые цветы"] = message.text
        users[user_id]["step"] = "sport"
        await message.answer("Введите ваш любимый вид спорта:")
    elif step == "sport":
        users[user_id]["Любимый спорт"] = message.text
        users[user_id]["step"] = "foot_size"
        await message.answer("Введите размер ноги:")
    elif step == "foot_size":
        users[user_id]["Размер ноги"] = message.text
        users[user_id]["step"] = "interests"
        await message.answer("Какие блюда вы любите?")
    elif step == "interests":
        users[user_id]["Любимые блюда"] = message.text
        users[user_id]["step"] = "movie_genre"
        await message.answer("Какой жанр фильма вам нравится?")
    elif step == "movie_genre":
        users[user_id]["Жанр фильма"] = message.text
        users[user_id]["step"] = "music_genre"
        await message.answer("Какую музыку вы любите?")
    elif step == "music_genre":
        users[user_id]["Жанр музыки"] = message.text
        users[user_id]["step"] = "favorite_color"
        await message.answer("Какой ваш любимый цвет?")
    elif step == "favorite_color":
        users[user_id]["Любимый цвет"] = message.text
        users[user_id]["step"] = "photo"
        await message.answer("Хотите ли вы добавить фото? (Отправьте 'Да' или 'Нет')")
    elif step == "photo":
        if message.text.lower() == "да":
            users[user_id]["step"] = "photo_upload"
            await message.answer("Пожалуйста, отправьте ваше фото.")
        else:
            users[user_id]["step"] = None
            await message.answer("Вы успешно зарегистрированы! Вы можете изменить профиль или просмотреть других.", reply_markup=main_menu)
    elif step == "photo_upload":
        if message.photo:
            file_id = message.photo[-1].file_id
            users[user_id]["Фото"] = file_id
            users[user_id]["step"] = None
            await message.answer("Фото успешно загружено! Вы успешно зарегистрированы.", reply_markup=main_menu)
        else:
            await message.answer("Пожалуйста, отправьте фото.")

@dp.message(F.text == "2) Увидеть других")
async def view_profiles(message):
    if not users:
        await message.answer("Пока никто не зарегистрировался.")
    else:
        result = []
        for user_id, data in users.items():
            if "Имя" in data:
                profile = "\n".join([f"{key}: {value}" for key, value in data.items() if key != "step"])
                result.append(profile)
        await message.answer("\n\n".join(result))

@dp.message(F.text == "3) Удалить профиль")
async def delete_profile(message):
    user_id = message.from_user.id
    if user_id in users:
        name_surname = f"{users[user_id]['Имя']} {users[user_id]['Фамилия']}"
        del users[user_id]
        names_surnames.discard(name_surname)
        await message.answer("Ваш профиль был удален.")
    else:
        await message.answer("Вы не зарегистрированы.")

if __name__ == "__main__":
    dp.run_polling(bot)

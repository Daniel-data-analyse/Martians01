import telebot
from telebot.types import BotCommand
from telebot import types
import webbrowser

bot = telebot.TeleBot('7887213288:AAGMjprwrUo24oIPKp8-EF8_VfBxON_1s38')

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton("open site")
    markup.row(button1)
    button2 = types.InlineKeyboardButton("Delete photo")
    button3 = types.InlineKeyboardButton("Edit")
    markup.row(button3, button2)
    bot.send_message(message.chat.id, 'Hello!', reply_markup=markup)


commands = [
    BotCommand("mangapoisk", "site to read manhwa"),
    BotCommand("youtube", "site to sea videos"),
    BotCommand("chatgpt", "AI"),
    BotCommand("ted", "chanel in youtube")
]

bot.set_my_commands(commands)

@bot.message_handler(commands=["mangapoisk"])
def open_mangapoisk(message):
    webbrowser.open("https://mangapoisk.live/")
    bot.send_message(message.chat.id, "opening a site mangapoisk...")

@bot.message_handler(commands=["youtube"])
def open_youtube(message):
    webbrowser.open("https://www.youtube.com/")
    bot.send_message(message.chat.id, "opening a youtube...")

@bot.message_handler(commands=["chatgpt"])
def open_AI(message):
    webbrowser.open("https://chatgpt.com/")
    bot.send_message(message.chat.id, "opening an AI...")

@bot.message_handler(commands=["ted"])
def open_ted(message):
    webbrowser.open("https://m.youtube.com/user/TEDxTalks")
    bot.send_message(message.chat.id, "opening TED...")

@bot.message_handler(content_types=["photo"])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Open Instagram", url="https://www.instagram.com/")
    markup.row(button1)
    button2 = types.InlineKeyboardButton("Delete photo", callback_data="delete")
    button3 = types.InlineKeyboardButton("Edit", callback_data="edit")
    markup.row(button3, button2)
    bot.reply_to(message, 'What a beautiful photo! Do you wnat to post it on Instagram?', reply_markup=markup)

@bot.message_handler(content_types=["video"])
def get_video(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Open YouTube", url="https://www.youtube.com/?hl=RU"))
    bot.reply_to(message, "What a good video! Do you want to share it with others?", reply_markup=markup)

@bot.message_handler(content_types=["animation"])
def get_gif(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Open WhatsApp", url = "https://www.whatsapp.com/?lang=ru_RU"))
    bot.reply_to(message, "WOW, very good GIF!", reply_markup=markup)

@bot.message_handler(commands=["start", "main", "hello"])
def main(message):
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}, чем могу вам помочь?")

@bot.message_handler()
def info(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}")
    elif message.text.lower() == "как дела?":
        bot.send_message(message.chat.id, f"Хорошо сам как?")
    elif message.text.lower() == "хорошо":
        bot.send_message(message.chat.id, f"Отлично!")

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id -1)
    elif callback.data == "edit":
        bot.edit_message_text("This message has been edited!",
                             callback.message.chat.id, 
                             message_id=callback.message.message_id)

bot.polling(none_stop=True)


import telebot
from models import *
from views import *

token = '5795074181:AAEYHOalWk9jR69mFeJvoHbo1BdPPXcym_g'
bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
button1 = telebot.types.KeyboardButton('Регистация пользователя:')
button2 = telebot.types.KeyboardButton('Регистация нарушения:')
button3 = telebot.types.KeyboardButton('Просмотр статуса нарушения:')
keyboard.add(button1, button2, button3)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите действие:)', reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите действие:)', reply_markup=keyboard)


@bot.message_handler(func=lambda m: True)
def check_answer(message):
    if message.text == 'Регистрация пользователя':
        create_user(message)
    elif message.text == 'Регистрация нарушения':
        create_complaint(message)
    elif message.text == 'Просмотр статуса нарушения':
        check_status(message)


bot.polling(non_stop=True)

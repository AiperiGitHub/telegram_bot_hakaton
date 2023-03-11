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
    answer = bot.send_message(message.chat.id, 'Добро пожаловать! Выберите действие:)', reply_markup=keyboard)
    bot.register_next_step_handler(answer, check_answer)


@bot.message_handler(func=lambda m: True)
def check_answer(answer):
    if answer.text == button1:
        create_user()
    elif answer.text == button2:
        create_complaint()
    elif answer.text == button3:
        check_status()











bot.polling(non_stop=True)

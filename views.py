from main import bot
from models import *


def create_user(message):
    bot.send_message(message.chat.id, 'Введите Ваше имя:')
    bot.register_next_step_handler(message, set_first_name)


def set_first_name(message):
    first_name = message.text
    bot.send_message(message.chat.id, 'Введите Вашу фамилию:')
    bot.register_next_step_handler(message, set_last_name, first_name=first_name)


def set_last_name(message, first_name):
    last_name = message.text
    bot.send_message(message.chat.id, 'Введите Ваш email:')
    bot.register_next_step_handler(message, set_email, first_name=first_name, last_name=last_name)


def set_email(message, first_name, last_name):
    email = message.text
    bot.send_message(message.chat.id, 'Введите пароль:')
    bot.register_next_step_handler(message, set_password, first_name=first_name, last_name=last_name, email=email)


def set_password(message, first_name, last_name, email):
    password = message.text
    bot.send_message(message.chat.id, 'Введите Ваш возраст:')
    bot.register_next_step_handler(message, set_age, first_name=first_name, last_name=last_name, email=email,
                                   password=password)


def set_age(message, first_name, last_name, email, password):
    age = message.text
    bot.send_message(message.chat.id, 'Введите Ваш пол:')
    bot.register_next

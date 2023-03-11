from models import *


def create_user():
    first_name = input('Введите Ваше имя:')
    last_name = input('Введите Вашу фамилию:')
    email = input('Введите Ваш email:')
    password = input('Введите пароль:')
    age = input('Введите Ваш возраст:')
    male = input('Введите Ваш пол:')
    city = input('Введите город:')
    Person.create(first_name=first_name, last_name=last_name, email= email, password=password, age=age,
                  male=male, city=city)
                
    
def create_complaint():
    person = input('Введите Ваш ID:')
    description = input('Введите описание нарушения:')
    photo = input('Прикрепите фото нарушения:')
    video = input('Прикрепите видео нарушения:')
    place = input('Место нарушения:')
    date_time = input('Введите дату и время нарушения:')
    Complaint.create(person=person, description=description, photo=photo, video=video,
                     place=place, date_time=date_time)

def check_status():
    if Complaint.approved:
        Complaint.approved = False
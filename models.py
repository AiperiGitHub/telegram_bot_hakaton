import peewee
from peewee import *


db = SqliteDatabase('complaints.db')


class ComplaintPhoto(Model):
    photo = ImageField(upload_to='complaint/')


class Person(Model):
    id = peewee.AutoField(unique=True)
    first_name = CharField()
    last_name = CharField()
    email = CharField(unique=True)
    password = CharField()
    age = IntegerField()
    male = CharField()
    city = CharField()

    class Meta:
        database = db


class Complaint(Model):
    person = ForeignKeyField(Person, backref='complaints')
    description = TextField()
    photo = ForeignKeyField(ComplaintPhoto, on_delete=models.SET_NULL)
    video = BlobField()
    place = TextField()
    date_time = DateTimeField()
    approved = BooleanField(null=True)

    class Meta:
        database = db


def initialize_db():
    db.connect()
    db.create_tables([Person, Complaint])

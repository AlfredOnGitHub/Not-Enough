from peewee import *
import random
db = SqliteDatabase('basedato.db')


class Nombres(Model):
    name = CharField()
    number = IntegerField()

    class Meta:
        database = db


class Apellidos(Model):
    surname = CharField()
    number = IntegerField()

    class Meta:
        database = db


def create_and_connect():
    db.connect()
    db.create_tables([Nombres, Apellidos], safe=True)


def gen():
    name = Nombres.create(name='Ana', number=0)
    name1 = Nombres.create(name='Belinda', number=1)
    name2 = Nombres.create(name='Carla', number=2)
    name3 = Nombres.create(name='Daniel', number=3)
    name4 = Nombres.create(name='Eduardo', number=4)
    name5 = Nombres.create(name='Francisco', number=5)
    name6 = Nombres.create(name='Germán', number=6)
    name7 = Nombres.create(name='Helena', number=7)
    name8 = Nombres.create(name='Irene', number=8)
    name9 = Nombres.create(name='Jaime', number=9)
    name10 = Nombres.create(name='Katarina', number=10)
    surname = Apellidos.create(surname='Alvarez', number=0)
    surname1 = Apellidos.create(surname='Benito', number=1)
    surname2 = Apellidos.create(surname='Costa', number=2)
    surname3 = Apellidos.create(surname='De la Paz', number=3)
    surname4 = Apellidos.create(surname='Espinosa', number=4)
    surname5 = Apellidos.create(surname='Fuertes', number=5)
    surname6 = Apellidos.create(surname='Guardado', number=6)
    surname7 = Apellidos.create(surname='Hastío', number=7)
    surname8 = Apellidos.create(surname='Inocente', number=8)
    surname9 = Apellidos.create(surname='Jupiter', number=9)
    surname10 = Apellidos.create(surname='Khalessi', number=10)


def get_npc(number):
    npcnombre = Nombres.select().where(Nombres.number == number).get()
    print("Nombre : {}".format(npcnombre.name))


def get_apellido(number):
    print("---------------"
          " INFORME NUMERO "
          ": "+str(random.randrange(9999, stop=None))+"-"
          "--------------")
    npcapellido = Apellidos.select().where(Apellidos.number == number).get()
    print("Apellido : {}".format(npcapellido.surname))


def family_members():
    for person in Nombres.select():
        print("Name : {}".format(person.name))
    for ape in Apellidos.select():
        print("Apellidos: {}".format(ape.surname))
    for x in Nombres.select():
        print("Edad : {}".format(random.randint(18, 60)))


def randomshit():
    edad = random.randint(18, 60)
    cuenta = random.randrange(99999999999999, stop=None)
    print("Edad : "+str(edad)+"\nNúmero de Cuenta : "+str(cuenta))

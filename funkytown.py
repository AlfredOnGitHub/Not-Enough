#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random


def tutorial():
    print("\033[1;30;47m--------------- TUTORIAL ---------------\n\n\033[0;m"
          "\nEres un trabajador de la empresa SynData."
          "Nos dedicamos a realizar transferencias de distintas cuentas"
          "bancarias a una propia. Ya te hemos asignado una, de hecho."
          "Toda decisión tiene una influencia en el juego.\n"
          "Te irán llegando informes, los cuales tendrás que comprobar"
          "que tengan la identificación correcta, se acepte su divisa"
          "y tenga efectivo para realizar el proceso que desée.\n"
          "Si uno de estos da como resultado un error, no DEBERÍAS aceptar"
          "el trámite."
          "\nSin más, creo que va siendo hora de probar el juego.\n\n"
          "\033[1;30;47m---------- FIN DEL TUTORIAL ----------\n\033[0;m")


def prensa1():
    print("\n\033[1;31;47m"+"\n-------------- SYNDATA NEWS --------------\n\n"
          "\033[3;34;47m"+"Buenos días, empleados.\n"
          "Aunque hemos tenido fallos significativos en el"
          "sistema y estamos buscando soluciones (y al"
          "responsable), la empresa ha seguido su evolución.\n"
          "Nos agrada saber que tenemos empleados competentes"
          "y leales a la empesa, y por ello os compartimos"
          "vuestra evolución en la empresa:\n"
          "EVOLUCIÓN : "+str(random.randint(30, 69))+"%\033[0;m"+"\n\n")


def prensa2():
    print("\n\033[1;31;47m"+"\n-------------- SYNDATA NEWS --------------\n\n"
          "\033[3;34;47m"+"Buenos días, empleados.\n"
          "Aunque hemos tenido fallos significativos en el"
          "sistema y estamos buscando soluciones (y al responsable),"
          "la empresa ha seguido su evolución.\n"
          "Nos agrada saber que tenemos empleados competentes"
          "y leales a la empesa, y por ello os compartimos"
          "vuestra evolución en la empresa:\n"
          "EVOLUCIÓN : "+str(random.randint(30, 69))+"%\033[0;m"+"\n\n")


def prensa3():
    print("\n\033[1;31;47m"+"\n-------------- SYNDATA NEWS --------------\n\n"
          "\033[3;34;47m"+"Buenos días.\n"
          "En vista de los acontecimientos y de la mala gestión"
          "de la empresa por parte de los empleados, nos vemos "
          "obligados a reducir la plantilla.\n"
          "Todos aquellos con una evolución inferior"
          "al 30% serán despedidos:\n"
          "EVOLUCIÓN : "+str(random.randint(1, 29))+"%\033[0;m"+"\n\n")


def guarda1():
    print("\n\033[1;37;41m"+"SUPERVISOR : Eh, tú. Has tenido una"
          "bajada esta semana. Espero que tengas mas cuidado la"
          "próxima vez."+"\033[0;m\n")


def guarda2():
    print("\n\033[1;37;41m"+"SUPERVISOR : Ten cuidado con lo que"
          "haces. Si la vez anterior fue un desastre, ahora es todavía"
          "peor. Parece que voy a tener que vigilarte..."+"\033[0;m\n")


def guarda3():
    print("\n\033[1;37;41m"+"SUPERVISOR : Bueno para nada. "
          "Eso es lo que eres."+"\033[0;m\n")


def ending1():
    print("Ending bueno.")


def ending2():
    print("Ending meh.")


def ending3():
    print("Ending malo.")


def narrador():
    print("\n*** Bueno, por un poco no pasará "
          "nada... ¿No? ***\n"+"\033[0;m")


def narrador1():
    print("\n*** Si la gente no se molesta ni en"
          "poner bien su identificación,"
          "¿por qué te ibas a molestar tú? ***\n"+"\033[0;m")


def narrador2():
    print("\n*** Hm, un trabajo bien hecho. ***\n"+"\033[0;m")


def narrador3():
    print("\n** Un pensamiento fugaz atraviesa tu mente:"
          "¿Esto está bien?. La tontería dura hasta que"
          "te das cuenta de que tú solo haces tu"
          "trabajo. ***\n"+"\033[0;m")


def narrador4():
    print("\n*** Que sorpresa, al fin uno en condiciones..."
          "Aunque no parece necesitarlo. ***\n"+"\033[0;m")


def narrador5():
    print("\n*** Es muy probable que el contable sepa de esto..."
          "Pero lo haces igualmente. ***\n"+"\033[0;m")


def dineros():
    print("\n\033[4;32;40m"+"$$$$$$$$$$$$$$$ "
          " - CONECTANDO CON EL NÚMERO DE CUENTA  - "
          "$$$$$$$$$$$$$$$"+"\033[0;m\n")
    time.sleep(1)
    print("Estableciendo red segura.")
    time.sleep(2)
    print("Realizando ejercicio financiero.")
    time.sleep(1)
    print("25%...")
    time.sleep(1)
    print("50%...")
    time.sleep(1)
    print("75%...")
    time.sleep(2)
    print("Transacción completada.\n")


def handicap():
        n = random.randint(0, 10)
        if n == 8:
                print("ERROR DE IDENTIFICACIÓN.\n"
                      "Se acepta su divisa.\n"
                      "Fondo suficiente.\n")
        elif n == 9:
                print("Idenficiación correcta.\n"
                      "NO SE ACEPTA SU DIVISA.\n"
                      "ERROR AL LEER FONDOS.\n")
        elif n == 10:
                print("Identificación correcta.\n"
                      "Se acepta su divisa.\n"
                      "FONDOS INSUFICIENTES\n")
        else:
                print("Idenficiación correcta.\n"
                      "Se acepta su divisa.\n"
                      "Fondo suficiente.\n"
                      "Parece que todo está en orden\n")

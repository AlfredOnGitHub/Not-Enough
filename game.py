#!/usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *
from bd import *
import player
import funkytown
import random
import time
jugador = player.play


def juego():
        npc = jugador.npc
        while npc <= 4:
                try:
                        get_apellido(random.randint(0, 10))
                        get_npc(random.randint(0, 10))
                        randomshit()
                        npc += 1
                        funkytown.handicap()
                        option = str(input("----> ¿Desviar fondos a tu cuenta?"
                                           "Si/No\nElección : ").capitalize())
                except ValueError:
                        option = str(input("----> ERROR."
                                           "¿Desviar fondos a tu cuenta?"
                                           "Si/No.\nElección : ").capitalize())
                else:
                        if option == "Si":
                                funkytown.dineros()
                                funkytown.narrador()
                                jugador.guarda += 1
                                jugador.status -= 1
                        else:
                                r = random.randint(1, 2)
                                if r == 1:
                                        funkytown.narrador1()
                                elif r == 2:
                                        funkytown.narrador2()

                                jugador.guarda -= 1
                                jugador.status += 1
                if jugador.guarda == 5:
                        funkytown.guarda1()
                elif jugador.guarda == 10:
                        funkytown.guarda2()
                elif jugador.guarda == 15:
                        funkytown.guarda3()
                elif jugador.guarda < 1:
                        jugador.guarda = 0

                if npc == 5 and 0 <= jugador.status <= 9:
                        funkytown.prensa1()
                elif npc == 5 and 10 <= jugador.status <= 14:
                        funkytown.prensa2()
                elif npc == 5 and jugador.status == 15:
                        funkytown.prensa3()
                elif jugador.status < 1:
                        jugador.status = 0

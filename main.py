#!/usr/bin/env python
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    import bd
    from funkytown import tutorial
    from game import juego



    while True:
        menu = str(input("Bienvenido a Not Enough v.0.3.\n"
                        "¿Qué quieres hacer?\n"
                        "1. Jugar al juego.\n"
                        "2. Ver el tutorial.\n"
                        "3. Exit.\nElección : "))
        print()
        if menu == "1":
            vuelta = 0
            while vuelta < 3:
                juego()
                vuelta += 1
            print("HAS TERMINADO LA DEMO.")
            break
        elif menu == "2":
            tutorial()
        elif menu == "3":
            print("¡Adiós!")
            break

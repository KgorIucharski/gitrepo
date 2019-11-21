#!/usr/bin/env python
# -*- coding: utf-8 -*-



    """
    Funkcja pobiera liczby od użytkownika dopóki ich suma 
    nie przekroczy wartosci 75. Na koniec drukuje sumę liczb.
    """
    suma = 0
    i = 0
    while suma < 75:
        liczba = int(input("Podaj liczbę: "))
        if i == 0 and liczba > 75:
            print("Nie chcesz za dużo?")
            continue
        suma = suma + liczba 
        i = i + 1

    print(suma)
    
def main(args):
    sumuj_liczby()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

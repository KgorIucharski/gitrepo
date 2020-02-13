#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kalkulator.py
#
wynik = 0

def liczby1():    
    liczba1 = int(input("podaj pierwszą liczbę: "))
    return liczba1
def liczby2():
    liczba2 = int(input("podaj drugą liczbę: "))
    return liczba2
   
def dodaj(wynik):
    global wynik
    wynik = liczba1 + liczba2
    
  
def odejmij(wynik):
    global wynik
    wynik = liczba1 - liczba2    
    
    
def podziel(wynik):
    global wynik
    wynik = liczba1 / liczba2
    
    
def pomnoz(wynik):
    global wynik
    wynik = liczba1 * liczba2
    
    
def main(args):
    operacja = input("jaką operację chcesz wykonać (+, -, /, *): ")
        if operacja == "+" :
            dodaj(liczba1, liczba2)
        
        elif operacja == "-" :
            odejmij(liczba1, liczba2)
        
        elif operacja == "/" :
            podziel(liczba1, liczba2)
        
        elif operacja == "*" :
            pomnoz(liczba1, liczba2)
            
        print(wynik)
            
    return 0
    


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-



def main(args):
   n = m = 0
    n = int(input("podaj liczbę początkową: "))
     m = int(input("podaj liczbe końcową: "))
    while n < 1:
        n = int(input("podaj liczbę początkową: "))
    while m < 1:
        m = int(input("podaj liczbe końcową: "))
    
    for i in range(n ,m + 1):
        
        print(i, '', end = '')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

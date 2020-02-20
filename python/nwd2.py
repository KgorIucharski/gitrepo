#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nwd2.py




def main(args):
    a=int(input(podaj liczbe: ))
    b=int(input(podaj liczbe: ))
    licznik = 0
    while a > b:
        licznik+= 1
        a %= b
        b-=a
        
    print("NWD ", a)
    print("licznik ", licznik)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
   
   a = int(input("podaj bok pierwszy: "))
   b = int(input("podaj bok drugi: "))
   c = int(input("podaj bok trzeci:"))
   
   # ~if a + b > c:
       # ~if b + c > a:
           # ~if a + b > c:
               # ~print("da sie")
                # ~return 0
    if a + b > c and b + c > b:
        print("da sie sbudowac")
    else:
        print("nie da sie")
        
    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

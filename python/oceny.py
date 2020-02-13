#!/usr/bin/env python
#
#  


def pobierzOceny():
    oceny = []
    ocena = int(input("podaj ocenę: "))
    while ocena > 0:
        if ocena < 7:
            oceny.append(ocena)
        else:
            print('Błędna ocena!')
        ocena = int(input('Podaj ocenę: '))
    return oceny
    
def liczSrednia(oceny):
    print(sum(oceny) / len (oceny))

def main(args):
    oceny = pobierzOceny()
    liczSrednia(oceny)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    
    
    


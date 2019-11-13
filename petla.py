


def main(args):
    suma = 0
    for i in range(3):
        liczba = int(input('podaj liczbę: '))
        suma = suma + liczba
        
    print(suma)    
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

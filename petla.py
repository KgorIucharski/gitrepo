

def sumuj_parzyste():
    suma = 0
    for i in range(0, 101, 2):
        #liczba = int(input('podaj liczbę: '))
        suma = suma + i
        
    print(suma)
    


def main(args):
    
    sumuj_parzyste()
    
    return 0
    
    suma = 0
    for i in range(3):
        liczba = int(input('podaj liczbę: '))
        suma = suma + liczba
        
    print(suma)    
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

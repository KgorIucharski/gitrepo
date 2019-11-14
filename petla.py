

def sumuj_parzyste(start, stop):
    suma = 0
    for i in range(start, stop+1, 2):
        #liczba = int(input('podaj liczbę: '))
        suma = suma + i
        
    print(suma)
    
    
def drukuj_nieparzyste(start, stop):
    
    if start % 2 == 0:
        start = start + 1 
    for i in range(start, stop+1, 2):
        
        
            print(i)
    


def main(args):
    start = int(input("podaj początek zakresu: "))
    stop =  int(input("podaj koniec zakresu: "))
    drukuj_nieparzyste(start, stop)
    
    return 0
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

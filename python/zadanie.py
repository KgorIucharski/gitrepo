def sumuj_naturalne(start,stop):
    suma = 0 
    for i in range(start, stop):
        suma = suma + i
    print(i, '', end = '')




def main(args):
    start = int(input("podaj liczbę początkową: "))
    stop = int(input("podaj liczbe końcową: "))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

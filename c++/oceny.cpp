/*
 
 */


#include <iostream>
using namespace std;

void pobierzOceny (int tb[], int n) {
    int ocena = 0;
    int i = 0;
    while (n > 0)    
    //for (int i=0; i < n; i++) 
    {
        cout << "podaj ocenę: " ;
        cin >> ocena;
        if (ocena > 0 && ocena < 7) {
            tb[i] = ocena;
            i++;
            n--;
        }   
    }
    
float liczSrednia(int tb[], int n) {
    int suma = 0
        for (int i = 0; i < n; i++) {
        cout << tb[i] << " ";
        
        }
}
    
    
}
        
        }
    }
int main(int argc, char **argv)
{   int n;
    cout << "ile ocen podasz? ";
    cin >> n;
    int oceny[n];
    pobierzOceny(oceny, n);
    
	return 0;
}


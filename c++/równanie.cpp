


#include <iostream>

using namespace std;

int main(int argc, char **argv) {
    int a;
    int b;
    float x;
	cout << "Witaj w C++";
   
    cout << "podaj liczbę a: ";
    cin >> a;	
    cout << "podaj liczbę b: ";
    cin >> b;
    if (a == 0) {
        if (b == 0) {
            cout << "nieskończenie wiele rozwiązań";
            } else {
                cout << "równaie sprzeczne"; 
            }
    } else {
        x = -b / (float)a;
        cout << x;
    }
	return 0;
}


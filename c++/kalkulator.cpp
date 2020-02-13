/*
 * kalkulator.cpp
 */


#include <iostream>
using namespace std;

void dodaj () {
        int a, b;
        cout << "podaj dwie liczby:" << endl;
        cin >> a >> b;
        cout << "suma: " <<a + b << endl;
void odejmij () {
        int a, b;
        cout << "podaj dwie liczby:" << endl;
        cin >> a >> b;
        cout << "suma: " <<a - b << endl;
}

int main(int argc, char **argv)
{
	char operacja;
    cout << "jakie działanie chcesz wuykonać (+, -, *, /)?"<< endl;
    cin >> operacja;
    switch(operacja) {
        case '+':
            dodaj();
        break;
        case '-':
            odejmij();
        break;
        case '/':
            dzielenie();
        default:
            cout << "nie rozumiem" << endl;
        break;
    }
	return 0;
}


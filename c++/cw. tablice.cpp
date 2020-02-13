



#include <iostream>
using namespace std;

void pobierzliczby(int t[], int n) {
    for (int i =0; i < n; i++) {
        cout << "podaj liczbę"; 
        cin >> t[i];
    }
}
void drukuj(int t[], int n) {
    for (int i =0; i < n; i++) {
        cout << t[i] << endl;
    }
    cout << endl;
}

int main(int argc, char **argv)
{
	int n = 5;
    int t1[n];
    int t2[n];
    pobierzliczby(t1, n);
    pobierzliczby(t2, n);
    drukuj(t1, n);
    drukuj(t2, n);
    
	return 0;
}


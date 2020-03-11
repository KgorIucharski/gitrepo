/*
 * sortowanie.cpp
 */


#include <iostream>
using namespace std;

void wypelnij(int tab[], int r, int maks){
     srand(time(NULL));
     for(int i=0; i<r; i++) {
            tab[i] = rand() % (maks + 1);
     }       
}
void drukuj(int tab[], int r){
     for(int i=0; i<r; i++) {
        cout << tab[i] << " ";
    }
    cout << endl;
}
void zamien (int t[], int i) {
    int tmp = t[i+1];
    t[i+1] = t[i];
    t[i] = tmp;
} 

void sort_bubble(int t[], int r){
    for (int j = r-1; j > 0; j--) {
        for (int i = 0; i < j; i++) {
            cout << i << "," << i+1 << " ";
            if (t[i] > t[i+1]) {
                zamien(t, i);
                }
            }
            cout << endl;
        }
    }

int main(int argc, char **argv)
{
	int r = 10;
    int maks = 100;
    int tab[r];wypelnij(tab, r, maks);
    drukuj(tab, r);
    sort_bubble(tab, r);
	return 0;
}


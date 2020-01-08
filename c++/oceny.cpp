/*
 
 */


#include <iostream>
using namespace std;


int main(int argc, char **argv)
{
	int a, b, c;
    cout << "podaj 3 oceny: " << endl;
    cin >> a >> b >> c;
    if (a == 0) {
        if (b == 0) {
            if (c == 0) {
                cout << "błędna liczba"; }
            }
        }
	return 0;
}


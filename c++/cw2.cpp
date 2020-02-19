

 
 


#include <iostream>
#include <iomanip>
using namespace std;

void wypelnij(int tab[][10], int w, int k, int n){
     srand(time(NULL));
     for(int i=0; i<w; i++) {
        for(int j=0; j<k; j++) {
            tab[i][j] = rand() % (n + 1);
            cout << i << "," << j << " " << tab[i][j] << endl;
            
            }
        }
    }
void sumujW(int tab[][10], int w, int k, int n){
    int sumaW = 0;
    for(int i=0; i<w; i++) {
        for(int j=0; j<k; j++) {
            cout << setw(4) << tab[i][j];
            sumaW += tab[i][j];
            }
            cout << setw(6) << sumaW << endl;
        } 
    //wydrukuj maksymalną sumę oraz indeks wiersza
    }
    

int main(int argc, char **argv)
{
	int n = 0 ;
    cout << "podaj wartość maksymalną: ";
    cin >> n;
    
    int w = 5;
    int k = 10;
    int tab[w][10];
    wypelnij(tab, w, k, n); 
    sumujW(tab, w, k, n);
	return 0;
}


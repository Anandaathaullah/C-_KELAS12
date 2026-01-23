#include <iostream>
using namespace std;
int main(){
	int n, angka, maks;
	cout << "Masukan banyak data: ";
	cin >> n;
	cout << "Masukan angka ke -1: ";
	cin >> maks;
	for (int i = 2; i <= n; i++) {
		cout << "Masukan angka ke -" << i << ": ";
		cin >> angka;
		if (angka > maks){
			maks = angka;
		}
	}
	cout << "Nilai maksimun adalah: " << maks << endl;
	return 0;
}
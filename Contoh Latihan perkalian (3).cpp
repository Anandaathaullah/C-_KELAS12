#include <iostream>
using namespace std;

int main() {
	int n, i = 1;
	cout << "Masukan angka untuk tabel perkalian: ";
	cin >> n;
	do {
		cout << n << " X " << i << " = " << n * i << endl;
		i++;
	} while (i <= 10);
	return 0;
}
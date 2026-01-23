#include <iostream>
using namespace std;

int tambah(int a, int b) {
	return a + b;
}
int main(){
	int hasil = tambah(4, 5);
	cout << "Hasil penjumlahan: " << hasil << endl;
	return 0;
}
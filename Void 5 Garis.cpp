#include <iostream>
using namespace std;

void garis() {
	cout << "========================" << endl;
}
void tampilJudul() {
	garis();
	cout << "PROGRAM DATA SISWA" << endl;
	garis();
}
int main(){
	tampilJudul();
	cout << "Nama: Siti Amirah" << endl;
	cout << "Kelas: X RPL" << endl;
	garis();
	return 0;
}
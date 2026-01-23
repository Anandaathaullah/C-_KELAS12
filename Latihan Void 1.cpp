#include <iostream>
using namespace std;
void garis() {
	cout << "=========================" << endl;
}
void tampilJudul() {
	garis();
	cout << "|> PROGRAM DATA HEWAN <|" << endl;
	garis();
}
int main(){
tampilJudul();
cout << "Nama Hewan: Burung Kakatua" << endl;
cout << "Jenis Kelamin: Jantan" << endl;
cout << "Warna: Merah" << endl;
cout << "Umur: 9 Bulan" << endl;
garis();
	return 0;
}
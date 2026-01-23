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

void garis1() {
	cout << "=========================" << endl;
}
void tampilJudul1() {
	garis1();
	cout << "|> PROGRAM DATA HEWAN <|" << endl;
	garis1();
}

void NamaSiswa1(string nama1) {
	cout << "Halo nama saya " << nama1 << ", salam kenal!" << endl;
}

void NamaSiswa2(string nama2){
	cout << "Salam kenal. Saya Putri dan ini " << nama2 << ", salam kenal juga" << endl;
}

void tampilPesan() {
	cout << "Selamat belajar C++ di SMK!" << endl;
}

void sapaSiswa(string nama) {
	cout << "Halo " << nama << ", semangat belajar C++!" << endl;
}

void hitungpersegi() {
	cout << "Hitung Luas Persegi Panjang" << endl;
}

void hitungLuasPersegiPanjang(int panjang, int lebar) {
	int luas = panjang * lebar;
	cout << "Luas persegi panjang: " << luas << endl;
}

void tampilNama(string nama, int jumlah) {
	for (int i = 1; i <= jumlah; i++) {
	cout << i << ". " << nama << endl;
	}
}
int main(){
	tampilJudul();
	cout << "Nama: Refan Putu" << endl;
	cout << "Kelas: XI RPL" << endl;
	garis();
	tampilJudul1();
cout << "Nama Hewan: Burung Kakatua" << endl;
cout << "Jenis Kelamin: Jantan" << endl;
cout << "Warna: Merah" << endl;
cout << "Umur: 9 Bulan" << endl;
garis();
tampilPesan(); // memanggil procedure
NamaSiswa1("Andi");
NamaSiswa2("Sausan");
sapaSiswa("Andi");
sapaSiswa("Angel");
hitungpersegi(); // memanggil procedure
hitungLuasPersegiPanjang(8,14);
tampilNama("Stereo", 10);
	return 0;
}
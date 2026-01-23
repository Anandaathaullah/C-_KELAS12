#include <iostream>
using namespace std;

void biodata(string nama, int umur){
	cout << "Nama: " << nama << endl;
	cout << "Umur: " << umur << " tahun" << endl;
}
int main(){
	biodata("Aulia", 16);
	biodata("Rizky", 17);
	return 0;
}
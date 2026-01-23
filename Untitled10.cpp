#include <iostream>
using namespace std;

void cetaknama(string nama) {
	cout << "Halo, " << nama << endl;
}
void biodata(string nama, int umur){
	cout << "Nama: " << nama << endl;
	cout << "Umur: " << umur << " tahun" << endl;
}
int main(){
	
	cetaknama("Budi");
	cetaknama("Siti");
	biodata("Aulia", 16);
	biodata("Rizky", 17);
	return 0;
}
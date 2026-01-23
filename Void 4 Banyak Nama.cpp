#include <iostream>
using namespace std;

void tampilNama(string nama, int jumlah) {
	for (int i = 1; i <= jumlah; i++) {
	cout << i << ". " << nama << endl;
	}
}
int main(){
	tampilNama("Andi", 3);
	return 0;
}
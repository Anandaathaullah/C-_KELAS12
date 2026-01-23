#include <iostream>
using namespace std;

char nilaiHuruf(int nilai) {
	if (nilai >= 90) return 'A';
	else if (nilai >= 80) return 'B';
	else if (nilai >= 70) return 'C';
	else return 'D';
}
int main(){
	cout << "Nilai Huruf: " << nilaiHuruf(85) << endl;
	return 0;
}
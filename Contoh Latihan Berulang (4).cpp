#include <iostream>
using namespace std;

int main(){
	string nama;
	int n;
	cout << "Masukan nama: ";
	cin >> nama;
	cout << "Mau ulang berapan kali? ";
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cout << i << ". " << endl;
	}
	return 0;
}
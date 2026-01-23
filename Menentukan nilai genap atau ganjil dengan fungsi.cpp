#include <iostream>
using namespace std;

bool isGenap(int x){
	return x % 2 == 0;
}
int main(){
	int bil;
	cout << "Masukan Bilangan: ";
	cin >> bil;
	if (isGenap(bil))
	cout << "Bilangan genap";
	else
	cout << "Bilangan ganjil";
	return 0;
}
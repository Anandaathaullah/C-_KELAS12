#include <iostream>
using namespace std;

int main(){
	int n, faktorial = 1;
	cout << "Masukan bilangan: ";
	cin >> n;
	int i = 1;
	while (i <= n) {
		faktorial *= i;
		i++;
	}
	cout << "Faktorial dari " << n << " adalah " << faktorial << endl;
	return 0;
}
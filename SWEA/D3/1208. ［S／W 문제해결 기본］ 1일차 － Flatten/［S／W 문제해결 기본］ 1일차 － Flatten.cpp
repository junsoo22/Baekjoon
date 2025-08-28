#include <iostream>
#include <algorithm>

using namespace std;

int box[100] = { 0 };

void flat(int& min, int& max) {
	min++;
	max--;
}

void print() {
	for(int i= 0; i < 100; i++) {
		cout << box[i] << " ";
	}
	cout << "\n";
}

int main() {

	for (int i = 1; i <= 10; i++) {
		int dump;
		cin >> dump;
		
		for (int j = 0; j < 100; j++) {
			cin >> box[j];
		}
		
		for (int j = 0; j < dump; j++) {
			sort(box, box + 100);
			//print();
			flat(box[0], box[99]);
			//print();
		}
		sort(box, box + 100);
		cout << "#" << i << " " << box[99] - box[0] << "\n";	

	}

}
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int arr[11];

int main() {
	int t;
	cin >> t;

	for (int i = 1; i <= t; i++) {

		for (int j = 1; j <= 10; j++) {
			cin >> arr[j];
		}
		sort(arr + 1, arr + 11);
		int sum = 0;
		for (int j = 2; j <=9; j++) {
			sum += arr[j];
		}
		double avg = sum / 8.0;
		cout << "#" << i << " " <<(int)round(avg) << "\n";
		

	}
}
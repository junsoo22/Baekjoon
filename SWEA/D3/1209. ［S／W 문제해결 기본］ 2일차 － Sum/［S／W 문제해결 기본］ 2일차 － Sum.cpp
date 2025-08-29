#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int arr[101][101];
vector<int>v;

int main() {
	
	for (int i = 1; i <= 10; i++) {
		int n;
		cin >> n;
		for(int j=0;j< 100; j++) {
			for(int k = 0; k < 100; k++) {
				cin >> arr[j][k];
			}
		}
		int row_sum = 0;
		int col_sum = 0;
		int dia1_sum = 0;
		v.clear();
		for(int j=0;j< 100; j++) {
			row_sum = 0;
			col_sum = 0;
			dia1_sum = 0;
			for (int k = 0; k < 100; k++) {
				row_sum += arr[j][k];
				col_sum += arr[k][j];
				dia1_sum += arr[k][k];
				
			}
			v.push_back(row_sum);
			v.push_back(col_sum);
			v.push_back(dia1_sum);
		}


		cout << "#" << i << " " << *max_element(v.begin(), v.end()) << "\n";
	}

}
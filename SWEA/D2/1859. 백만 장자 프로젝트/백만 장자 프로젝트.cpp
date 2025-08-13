#include <iostream>
#include <vector>

using namespace std;

vector<long long>v;
long long arr[1000001];

int main() {

	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		long long n;
		cin >> n;
		long long sum = 0;
		for (int j = 0; j < n; j++) {
			cin >> arr[j];
		}
		int maxx = arr[n-1];
		for (int k = n-2; k >=0; k--) {
			if(arr[k]<maxx){
				sum+=maxx - arr[k];
			}
			else {
				maxx = arr[k];
			}
		}
		cout <<"#"<<i+1 <<" " << sum << "\n";

	}
}
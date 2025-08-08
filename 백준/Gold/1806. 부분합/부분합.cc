#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;



int main() {
	int n, s;
	cin >> n >> s;
	vector<int>v;
	vector<int>sumV;
	v.resize(n);
	
	for (int i = 0; i < n; i++) {
		cin >> v[i];
	}

	int start = 0;
	int end = 0;
	int cnt = 0;
	int minLen = 1000000;
	int sum = 0;
	while (start<=end) {
		if (sum >= s) {
			minLen = min(minLen, end - start);
			sum -= v[start++];
		}
		else if (end == n) {
			break;
		}
		else {
			sum += v[end++];
		}
	}
	if (minLen == 1000000) {
		cout << 0 << "\n";

	}
	else {
		cout << minLen << "\n";
	}


}
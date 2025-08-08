#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<long long> v;
long long arr[100001];
int n, m, k;

long long init(int node, int start, int end) {
	if (start == end)
		return v[node] = arr[start];
	int mid = (start + end) / 2;
	return v[node] = min(init(node * 2, start, mid), init(node * 2 + 1, mid + 1, end));
}

long long update(int idx, int val, int node, int start, int end) {
	if (idx < start || end < idx) {
		return v[node];
	}
	if (start == end) {
		return v[node] = val;
	}
	int mid = (start + end) / 2;
	return v[node] = min(update(idx, val, node * 2, start, mid) , update(idx, val, node * 2 + 1, mid + 1, end));
}

long long find(int left, int right, int node, int start, int end) {
	if(left>end || right < start) {
		return 1e9; // Return a large value for min query
	}
	if(left <= start && end <= right) {
		return v[node];
	}
	int mid = (start + end) / 2;
	return min(find(left, right, node * 2, start, mid), find(left, right, node * 2 + 1, mid + 1, end));	
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n, m;
	cin >> n;
	v.resize(n * 4);
	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
	}
	init(1, 1, n);

	cin >> m;
	for (int i = 1; i <= m; i++) {
		int a, b,c;
		cin >> a >> b >> c;
		if (a == 1) {
			update(b, c, 1, 1, n);
		}
		else if (a == 2) {
			cout << find(b, c, 1, 1, n) << "\n";
		}


	}

}
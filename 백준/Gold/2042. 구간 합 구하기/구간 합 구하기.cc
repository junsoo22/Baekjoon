#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<long long> v;
long long arr[1000001];
int n, m, k;

long long init(int node, int start, int end) {
	if (start == end)
		return v[node] = arr[start];
	int mid = (start + end) / 2;
	return v[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end);
}

void update(int index, long long value, int node, int start, int end) {
	if (index < start || end < index)
		return;
	v[node] += value;
	if (start == end)
		return;
	int mid = (start + end) / 2;
	update(index, value, node * 2, start, mid);
	update(index, value, node * 2 + 1, mid + 1, end);
}

long long sum(int left, int right, int node, int start, int end) {
	if (left > end || right < start)
		return 0;
	if (left <= start && end <= right)
		return v[node];
	int mid = (start + end) / 2;
	return sum(left, right, node * 2, start, mid) + sum(left, right, node * 2 + 1, mid + 1, end);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	cin >> n >> m >> k;   //m: 변경 횟수, k: 구간의 합을 구하는 횟수
	v.resize(n * 4);
	long long num;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		
	}
	init(1, 0, n-1);   //트리 초기화
	for (int i = 0; i < m + k; i++) {
		long long a, b;
		long long c;
		cin >> a >> b >> c;
		if (a == 1) {
			long long temp = c-arr[b - 1];
			arr[b - 1] = c;
			update(b-1, temp, 1, 0,n-1);
		}
		else if (a == 2) {
			cout << sum(b-1, c-1, 1,0, n-1) << "\n";

		}
	}




}
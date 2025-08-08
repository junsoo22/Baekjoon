#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

priority_queue<int> pq1;  //내림차순 정렬: 중앙값 오른쪽 배열
priority_queue<int, vector<int>, greater<int>> pq2;    //오름차순 정렬: 중앙값 왼쪽 배열

int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	cin >> n;
	int num;
	int idx = 0;
	for (int i = 0; i < n; i++) {
		cin >> num;
		
		if (pq1.empty()) {
			pq1.push(num);
		}
		else if (pq1.size() == pq2.size()) {
			pq1.push(num);
		}
		else {
			pq2.push(num);
			
		}
		if (!pq1.empty() && !pq2.empty() && (pq1.top() > pq2.top())) {
			int a = pq1.top();
			int b = pq2.top();
			pq1.pop();
			pq2.pop();
			pq1.push(b);
			pq2.push(a);
		}
		cout << pq1.top() << "\n";
	}
}

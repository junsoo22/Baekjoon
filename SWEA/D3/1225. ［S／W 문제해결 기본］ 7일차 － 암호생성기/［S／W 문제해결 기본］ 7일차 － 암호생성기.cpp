#include <iostream>
#include <vector>
#include <deque>
#include <queue>
using namespace std;

queue<int>q;

void cycle() {
	for (int i = 0; i < 5; i++) {
		int temp = q.front();
		temp -= i + 1;
		if (temp <= 0) {
			temp = 0;
			q.pop();
			q.push(temp);
			return;
		}
		q.pop();
		q.push(temp);

	}

}

int main() {

	for (int i = 1; i <= 10; i++) {
		int n;
		cin >> n;

		for (int j = 0; j < 8; j++) {
			int num;
			cin >> num;
			q.push(num);
		}
		int cycle = 1;
		while (1) {
			int first = q.front();
			first -= cycle;
			q.pop();
			if (first <= 0) {
				break;
			}
			q.push(first);
			cycle+=1;
			if (cycle > 5) {
				cycle = 1;
			}
			
		}
		q.push(0);
		cout << "#" << i << " ";
		for (int j = 0; j < 8; j++) {
			cout << q.front() << " ";
			q.pop();
		}
		cout << "\n";

	}

}
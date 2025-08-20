#include <iostream>
#include <vector>
using namespace std;


vector<int> dp[100];

int main() {

	int t;
	cin >> t;
	for (int tc = 0; tc < t; tc++) {
		int n;
		cin >> n;
		for (int i = 0; i < n; i++) {
			dp[i].assign(i + 1, 0);
		}

		dp[0][0] = 1;
		dp[1][0] = 1;
		dp[1][1] = 1;
		for (int j = 2; j < n; j++) {
			dp[j][0] = 1;
			dp[j][j] = 1;
			for (int k = 1; k < j; k++) {
				dp[j][k] = dp[j - 1][k - 1] + dp[j - 1][k];
			}
		}

		cout << "#" << tc + 1 << "\n";
		for(int j = 0; j < n; j++) {
			for (int k = 0; k <= j; k++) {
				cout << dp[j][k] << " ";
			}
			cout << "\n";
		}
	}


}
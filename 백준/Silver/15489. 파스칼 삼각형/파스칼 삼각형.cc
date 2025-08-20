#include <iostream>
#include <vector>
using namespace std;


vector<int> dp[900];

int main() {

	int r, c, w;
	cin >> r >> c >> w;
	for (int i = 0; i < r + w; i++) {
		dp[i].resize(i + 1);
	}	
	dp[0][0] = 1;
	dp[1][0] = 1;
	dp[1][1] = 1;
	for (int i = 2; i < r + w; i++) {
		dp[i][0] = 1;
		dp[i][i] = 1;
		for (int j = 1; j < i; j++) {
			dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
		}
	}
	long long sum = 0;

	for (int i = 0; i < w; i++) {
		for(int j=0; j <= i; j++) {
			sum += dp[r - 1 + i][c - 1 + j];
		}
	}
	cout << sum;



}
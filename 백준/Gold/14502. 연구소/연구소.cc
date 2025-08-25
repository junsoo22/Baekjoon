#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int arr[9][9];
int tmp[9][9];
int ans;
int n, m;

int getSafeZone() {
	int cnt = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (tmp[i][j] == 0)
				cnt++;
		}
	}
	return cnt;
}

void virusDFS(int x, int y) {
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];	
		int ny = y + dy[i];	
		if(nx >= 1 && nx <= n && ny >= 1 && ny <= m) {
			if (tmp[nx][ny] == 0) {
				tmp[nx][ny] = 2;
				virusDFS(nx, ny);
			}
		}
	}

}

void dfs(int wall) {
	if (wall == 3) {
		for (int i = 1; i <= n; i++){
			for (int j = 1; j <= m; j++) {
				tmp[i][j] = arr[i][j];
			}
		}

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				if (tmp[i][j] == 2) {
					virusDFS(i, j);
				}
			}
		}

		ans = max(ans, getSafeZone());
		return;
	}

	for (int i = 1; i <= n; i++) {
		for(int j=1; j<=m; j++) {
			if(arr[i][j] == 0) {
				arr[i][j] = 1;
				dfs(wall+1);
				arr[i][j] = 0;
			}
		}
	}
	
	
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	cin>>n>>m;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			cin >> arr[i][j];
		}
	}
	dfs(0);
	cout << ans << "\n";
}
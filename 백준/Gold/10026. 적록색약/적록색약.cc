
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
using namespace std;

vector<char> g[101];
int visited[101][101];
int dx[4] = { -1,0,1,0 };
int dy[4] = { 0,-1,0,1 };
int n;

void dfs(int x, int y) {
	visited[x][y] = 1;	
	int cur = g[x][y];

	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];	
		int ny = y + dy[i];	
		if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny] && cur==g[nx][ny]) {
			visited[nx][ny] = 1;
			dfs(nx, ny);
		}	
	}
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++){
		string str;
		cin >> str;
		for (int j = 0; j < str.size(); j++) {
			g[i].push_back(str[j]);
		}
	}

	int cnt1 = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!visited[i][j]) {
				dfs(i, j);
				cnt1+=1;
			}
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			visited[i][j] = 0;
			if(g[i][j]== 'G') {
				g[i][j] = 'R';  // Change 'G' to 'R' for color-blindness simulation
			}	
		}
	}

	int cnt2 = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!visited[i][j]) {
				dfs(i, j);
				cnt2 += 1;
			}
		}
	}

	cout << cnt1<<" "<<cnt2;
}
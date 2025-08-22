
#include <iostream>
using namespace std;

int arr[9];
int n, m;

void dfs(int cnt, int start) {
    if (cnt == m) { // m개를 뽑았으면 출력
        for (int i = 0; i < m; i++) {
            cout << arr[i] << " ";
        }
        cout << "\n";
        return;
    }
    for (int i = start; i <= n; i++) {
        arr[cnt] = i;         // 현재 수 선택
        dfs(cnt + 1, i + 1);  // 다음 수는 i보다 큰 수만 선택
    }
}

int main() {
    cin >> n >> m;
    dfs(0, 1); // 1부터 시작
}

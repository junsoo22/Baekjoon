#include <iostream>
using namespace std;

int arr[16][16];

int main() {
    int t;
    cin >> t;

    for (int tc = 1; tc <= t; tc++) {
        int n, k;
        cin >> n >> k;

        // 입력
        for (int row = 1; row <= n; row++) {
            for (int col = 1; col <= n; col++) {
                cin >> arr[row][col];
            }
        }

        int result = 0;

        // 가로 검사
        for (int row = 1; row <= n; row++) {
            int flag = 0;
            for (int col = 1; col <= n; col++) {
                if (arr[row][col] == 1) {
                    flag++;
                } else {
                    if (flag == k) result++;
                    flag = 0;
                }
            }
            if (flag == k) result++; // 마지막 칸까지 갔을 때
        }

        // 세로 검사
        for (int col = 1; col <= n; col++) {
            int flag = 0;
            for (int row = 1; row <= n; row++) {
                if (arr[row][col] == 1) {
                    flag++;
                } else {
                    if (flag == k) result++;
                    flag = 0;
                }
            }
            if (flag == k) result++;
        }

        cout << "#" << tc << " " << result << "\n";
    }
}

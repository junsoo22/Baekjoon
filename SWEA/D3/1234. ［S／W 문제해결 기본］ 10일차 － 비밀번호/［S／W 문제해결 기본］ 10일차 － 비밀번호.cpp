#include <iostream>
#include <string>
#include <stack>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    for (int t = 1; t <= 10; t++) {
        int n;
        string pwd;
        cin >> n >> pwd;

        stack<char> st;
        for (char c : pwd) {
            if (!st.empty() && st.top() == c) {
                st.pop();  // 같은 문자가 연속되면 제거
            }
            else {
                st.push(c);
            }
        }

        // 스택에는 결과 문자열이 거꾸로 저장됨
        string result;
        while (!st.empty()) {
            result.push_back(st.top());
            st.pop();
        }
        reverse(result.begin(), result.end());

        cout << "#" << t << " " << result << "\n";
    }
}
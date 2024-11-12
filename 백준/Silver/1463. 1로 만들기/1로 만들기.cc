#include <iostream>
 #include <algorithm>
 using namespace std;
 int dp[1'000'005], N;
 int f(int x){
 if (x == 1) return 0;
 if (dp[x]) return dp[x];
 dp[x] = f(x-1) + 1;
 if (x % 2 == 0)
 dp[x] = min(dp[x], f(x/2) + 1);
 if (x % 3 == 0)
 dp[x] = min(dp[x], f(x/3) + 1);
 return dp[x];
 }
 int main(){
 cin >> N;
 cout << f(N);
 }
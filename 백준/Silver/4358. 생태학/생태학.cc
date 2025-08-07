#include <iostream>
#include <string>
#include <queue>
#include <map>
#include <vector>
#include <iomanip>

using namespace std;

int main() {
	string str;
	map<string, int> mp;
	int cnt = 1;
	int total = 0;
	cout << fixed << setprecision(4);
	while (getline(cin,str)) {
		
		if (mp.find(str) != mp.end()) {
			cnt += 1;
			mp[str] ++;
			total += 1;
		}
		else {
			cnt = 1;
			mp[str] = cnt;
			total += 1;
		}
		
	}

	for (auto itr = mp.begin(); itr != mp.end(); itr++) {
		cout << itr->first << " " << (double)itr->second /total* 100 << "\n";
		

	}


}
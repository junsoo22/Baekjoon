#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;

string num[10]= { "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN" };

int main() {
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		string str;
		
		int len;
		cin >> str>>len;
		vector<int>v;
		v.resize(10);
		for (int j = 0; j < len; j++) {
			string str2;
			cin >> str2;
			for (int k = 0; k < 10; k++) {
				if (num[k] == str2) {
					v[k]+=1;
					break;
				}
			}
			
			

		}
		cout << str << "\n";
		for (int j = 0; j < 10; j++) {
			for (int k = 0; k < v[j]; k++) {
				cout << num[j] << " ";
				}
			}
		cout << "\n";

	}

}
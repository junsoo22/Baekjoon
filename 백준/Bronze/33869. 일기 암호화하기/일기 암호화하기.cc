#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main() {

	string w, s;
	cin >> w;
	cin >> s;
	vector<char>c;

	string temp = "";
	for (char c : w) {
		if (temp.find(c) == string::npos) {
			temp += c;
		}
	}

	int cnt = 0;
	for (char c = 'A'; c <= 'Z';c++) {
		if (temp.find(c) == string::npos) {
			temp += c;
		}

	}
	map<char, char>m;
	for (int i = 0; i < 26; i++) {
		char plain = 'A' + i;
		char cipher = temp[i];
		m.insert({ plain, cipher });

	}
	for (char c : s) {
		if (c == ' ') {
			cout << " ";
		}
		else {
			cout << m[c];
		}
	}
	


}
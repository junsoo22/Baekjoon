#include <iostream>
#include <string>
#include <vector>
#include <list>
using namespace std;




int main() {
	for (int i = 1; i <= 10; i++) {

		int n;
		cin >> n;
		list<int>v;
		for (int j = 0; j < n; j++) {
			int w;
			cin >> w;
			v.push_back(w);
		}

		int k;
		cin >> k;
		for (int j = 0; j < k; j++) {
			string str;
			int x, y;
			cin >> str;
			if (str == "I") {
				cin >> x >> y;
				auto itr = v.begin();
				list<int>tmp;
				for (int num = 0; num < x; num++) {
					itr++;
				}
				for (int num = 0; num < y; num++) {
					int s;
					cin >> s;
					tmp.push_back(s);
				}
				v.splice(itr, tmp);

			}
			else if (str == "D") {
				cin >> x >> y;
				auto itr = v.begin();
				advance(itr, x);  //x번째 위치로 이동
				auto itr2 = itr;
				advance(itr2, y);
				v.erase(itr, itr2);
			}
			
		}

		cout << "#" << i << " ";
		auto itr = v.begin();
		for (int j = 0; j < 10; j++, itr++) {
			cout << *itr << " ";
		}
		cout << "\n";
	}
}
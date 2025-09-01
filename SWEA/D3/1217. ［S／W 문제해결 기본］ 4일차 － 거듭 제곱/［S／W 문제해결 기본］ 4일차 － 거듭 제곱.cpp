#include <iostream>
using namespace std;

int a, b;

int rec(int num,int count) {
	
	if (count==1) {
		return num;
	}
	return num * rec(num,count-1);
}

//1217 거듭제곱
int main() {
	for (int i = 1; i <= 10; i++) {
		int n;
		cin >> n;
		int a, b;
		cin >> a >> b;
		cout<<"#"<<i<<" " << rec(a, b)<<"\n";
		

	}

}
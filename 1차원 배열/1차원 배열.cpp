#include <iostream>
#include <vector>
using namespace std;

//3052번
int main() {
	int arr[42] = {};
	int num;
	for (int i = 0; i < 10; i++) {
		cin >> num;
		arr[num % 42] = 1;
	}
	int result = 0;
	for (int i = 0; i < 42;i++) {
		result += arr[i];
	}
	cout << result;
}

//10813번
//int main() {
//	int N, M;
//	int num1, num2;
//	int tmp1, tmp2;
//
//	cin >> N >> M;
//	int arr[100];
//	for (int i = 0; i < N; i++) {
//		arr[i] = i + 1;
//	}
//	for (int i = 0; i < M; i++) {
//		cin >> num1 >> num2;
//		tmp1 = arr[num1 - 1];
//		arr[num1 - 1] = arr[num2 - 1];
//		arr[num2 - 1] = tmp1;
//	}
//	for (int i = 0; i < N; i++) {
//		cout << arr[i] << " ";
//	}
//}

//10810번
//int main() {
//	int N, M;
//	int start, end, num;
//	vector <int> arr1;
//	cin >> N >> M;
//	arr1.resize(N);
//	for (int i = 0; i < M; i++) {
//		cin >> start >> end >> num;
//		for (int j = start - 1; j <= end - 1; j++) {
//			arr1[j] = num;
//		}
//	}
//	for (int i = 0; i < N; i++) {
//		cout << arr1[i]<<" ";
//	}
//}


//2562번
//int main() {
//	int max = 0;
//	vector<int> arr(9);
//	int index = 0;
//	for (int i = 0; i < 9; i++) {
//		cin >> arr[i];
//	}
//	for (int i = 0; i < 9; i++) {
//		if (arr[i] > max) {
//			max = arr[i];
//			index = i;
//		}
//	}
//	cout << max << "\n" << index;
//}

//10807번
//int main() {
//	int num;
//	int find;
//	int cnt = 0;
//	vector<int> arr;
//	cin >> num;
//	arr.resize(num);
//	for (int i = 0; i < num; i++) {
//		cin >> arr[i];
//	}
//	cin >> find;
//
//	for (int i = 0; i < num; i++) {
//		if (arr[i] == find) {
//			cnt++;
//		}
//	}
//	cout << cnt;
//	
//	return 0;
//}
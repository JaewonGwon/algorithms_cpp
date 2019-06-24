#include<iostream>
#define MAX 1000000 
#define SWAPPER(x, y) { int t = x; x = y; y = t; } 
int N, arr[MAX]; 
using namespace std;

void qSort(int *array, int left, int right) {
	int mLeft = left, mRight = right;
	int pivot = array[(left + right) / 2];

	while (mLeft <= mRight) {
		while (pivot > array[mLeft]) mLeft++;
		while (pivot < array[mRight]) mRight--;

		if (mLeft <= mRight) {
			SWAPPER(array[mLeft], array[mRight]);
			mLeft++, mRight--;
		}
	}

	if (left < mRight) qSort(arr, left, mRight);
	if (mLeft < right) qSort(arr, mLeft, right);
}

int main() {
	int idx;
    int N = 0;
	cin >> N;
	for (idx = 0; idx < N; idx++) {
		cin >> arr[idx];
	}

	qSort(arr, 0, N - 1);  

	for (idx = 0; idx < N; idx++) {
		cout << arr[idx] << "\n";
	}
	return 0;
}
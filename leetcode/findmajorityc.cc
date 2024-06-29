// C++ program to find Majority
// element in an array
#include <bits/stdc++.h>
using namespace std;

// Function to find Majority element
// in an array
void findMajority(int arr[], int n) {

	int arr1[n];
	for (int i = 0; i < n; i++) {
		int count = 0;
		for (int j = i; j < n; j++) {
			if (arr[i] == arr[j]) {
				count++;
			}
		}
		if (count > (n / 3)) {
			arr1[i]=arr[i];
			//cout<<sizeof(arr1);
		}
	}
	cout<<(sizeof(arr1) / sizeof(arr1[0]));
	for(int i =0;i<(sizeof(arr1) / sizeof(arr1[0]));i++)
	{
		//cout<<(arr1[i]);
	}
}
int main() {

	int arr[] = { 2, 2, 3, 1, 3, 2, 1, 1 };
	int n = sizeof(arr) / sizeof(arr[0]);

	// Function calling
	findMajority(arr, n);
	return 0;
}

// This code is contributed by Aman Chowdhury

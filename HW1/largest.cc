// Program to find the largest element of an array

#include<iostream>
#include<time.h>
using namespace std;

int large(int *arr, int n)
{
	// Iterates over the array and finds the largest element
	int max=arr[0];
	for(int i=1;i<n;i++)
		if(arr[i]>max)
			max=arr[i];
	return max;
}

int main()
{
	// Creates a 15 element array of random positive integers less than 20  and passes it to large(int*, int). Displays the result of this call as well.
	srand(time(0));
	int size=15;
	int arr[size]={rand()%20,rand()%20,rand()%20,rand()%20,rand()%20,rand()%20,rand()%20,rand()%20,rand()%20,rand()%20,rand()%20,rand()%20,rand()%20,rand()%20,rand()%20};
	cout << "The randomly generated array is :\n" << arr[0];
        for(int i=1;i<size;i++)
                cout << ", " << arr[i];
        cout << "\n" << endl;
	cout << "The largest value in the array is : " << large(arr,size) << endl;
	return 0;
}

// Program to find that n largest elements from an array

#include<iostream>
#include<time.h>
using namespace std;

void nlarge(int *arr,int s,int n)
{
	// Implements a partial selection sort in descending order so that the n largest elements become the first n elements of the input array. Sorting is done inplace so no return required
        for(int i=0;i<n;i++)
        {
                int index=i;
                for(int j=i+1;j<s;j++)
           	     if(arr[j]>arr[index])
                        {
                                int tmp=arr[j];
                                arr[j]=arr[index];
                                arr[index]=tmp;
                        }
        }
}

int main()
{
	// Creates a 15 element array of random positive integers less than 20  and passes it to nlarge(int*, int). Displays the result of this call as well.
	srand(time(0));
        int size=15,n=0;
        int arr[size];
	for(int i=0;i<size;i++)
		arr[i]=rand()%20;
	cout << "The randomly generated array is :\n" << arr[0];
	for(int i=1;i<size;i++)
		cout << ", " << arr[i];
	cout << "\n" << endl;
	cout << "Enter the number of largest values required : ";
	cin >> n;
	cout << "\n";
	nlarge(arr,size,n);
	cout << "The " << n << " largest values in the array in order are : " << arr[0];
	for(int i=1;i<n;i++)
		cout << ", " << arr[i];
	cout << endl;
        return 0;
}

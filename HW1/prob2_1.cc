#include<iostream>
using namespace std;

int sorting(int arr[],int l) {
	int temp; int i;
	temp=0;
	for(i=1; i<l;i++)
		if(arr[0]<arr[i]) {
			temp=arr[0];
			arr[0]=arr[i];
			arr[i]=temp;
		}
	cout<<arr[0]<<endl;
}

int main() {
	int array[]={10,34,87,3,89,23,45,67,190,78,56,90,21,45,87,43,90};
	int l=sizeof(array)/sizeof(array[0]);
	sorting(array,l);
}

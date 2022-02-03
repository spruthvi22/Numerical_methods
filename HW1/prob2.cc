#include<iostream>
using namespace std;

int sorting(int arr[],int l,int n) {
	int temp;int i;int j;
	for(i=0; i<l-1; i++)
		for(j=i+1;j<l; j++)
			
		        if(arr[i]<arr[j]) {
		        	temp=arr[i];
		        	arr[i]=arr[j];
		
				arr[j]=temp;	
        	}
	for(int m=0;m<n;m++)
		cout<<arr[m]<<endl;

}

int main() {
      int n;	
      int array[]={10,34,87,3,89,23,45,67,190,78,56,90,21,45,87,43,90};
      cout<<"enter the value of n: "<<endl;
      cin>>n;

      int l=sizeof(array)/sizeof(array[0]);
      cout<<"the top n largest numbers are: "<<endl;
      sorting(array,l,n);
      
     
      return 0;
}






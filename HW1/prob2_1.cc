#include<iostream>
using namespace std;
float max(float *a, int n){
	float b=*a;
	for(int i=0;i<n;i++){
	    if(b<*a){
	     b=*a;
	    }
            a++; 
	}
        return b;
}
int main(){
	float a[6]={10,20,2,35,76.5,8};
	float c;
	c=max(a,6);
	cout<<"The largest number in the array is"<<c<<endl;
	return 0;
}

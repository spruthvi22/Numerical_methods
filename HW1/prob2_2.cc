#include<iostream>
using namespace std;
float * max(float *a, int m, int n){
        static float r[100];
	float *b;
	for(int i=0;i<m;i++){
		r[i]=*a;
		b=a;
		for(int j=0;j<n;j++){
			if(r[i]<*a){
			       r[i]=*a;
			       b=a;
		               cout<<b<<"  ";
		               cout<<*b<<endl;	       
			}
		        a++;	
                }
	        *b=-1e6;
		a=a-n;
	}
        return r;
}

int main(){
	float *d;
	int K;
	float R[20]={10,11.3,22,-90,30,87,556,0.987,0.56,23.8,-900,1235,12,123,76,89,5675,90,456,1000};
	cout<<"Enter the number of values to be displayed:";
	cin>>K;
	d=max(R,K,20);
	for(int h=0;h<K;h++){
		cout<<*(d+h)<<endl;
	}
	return 0;
}
				      


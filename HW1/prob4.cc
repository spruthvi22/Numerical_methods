#include<iostream>
#include<chrono>
using namespace std;
using namespace std::chrono;

float sequence(int n) {
	float temp1=0.0; float temp2=1.0; float term=0.0;
	for(int i=1 ; i<n ; ++i) {
		term=temp1+temp2;
		temp1=temp2;
		temp2=term;
	}
	return term;
}

int main() {
	float nth_term; int n;
	cout<<"enter the value of n: ";
	cin>>n;
	auto begin=std::chrono::high_resolution_clock::now();
	nth_term=sequence(n);
	auto stop=std::chrono::high_resolution_clock::now();
	auto duration=duration_cast<nanoseconds>(stop-begin);
	cout<<duration.count()<<"nanoseconds"<<endl;
	cout<<"The nth term is: "<<nth_term<<endl;
	return 0;

}



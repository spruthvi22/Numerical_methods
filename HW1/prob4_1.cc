#include<iostream>

#include<chrono>
using namespace std;
long fibonacci(int n){
	if (n<2){
		return n;
	}
	return fibonacci(n-1)+fibonacci(n-2);
}
int main(){
	std::chrono::time_point<std::chrono::high_resolution_clock> start, end;
	start=std::chrono::high_resolution_clock::now();
	cout<<"f(43) = "<<fibonacci(43)<<'\n';
	end=std::chrono::high_resolution_clock::now();
	std::chrono::duration<double> elapsed_time=end - start;
        cout<<"finished computation in time : "<<elapsed_time.count()<<endl;
	return 0;
}


// Program to find the nth Fibonacci number and find the time taken to do so

#include<iostream>
#include<chrono>
using namespace std;
using namespace std::chrono;

float fib(int n)
{
	// Finds the nth Fibonacci number using the recurrence relation
	float f1=0.0,f2=1.0,f3=0.0;
	if(n==1)
		return f1;
	if(n==2)
		return f2;
	for(int i=3;i<=n;i++)
	{
		f3=f1+f2;
		f1=f2;
		f2=f3;
	}
	return f3;
}

int main()
{
	// Calls fib(int) to get the nth Fibonacci number and uses the chrono library to record the time taken in said function call. Both are then output to console.
	int n;
	cout << "Enter the value of n : ";
	cin >> n;
	auto begin=high_resolution_clock::now();
	cout << "\nThe required Fibonacci number is : " << fib(n) << endl;
	auto end=high_resolution_clock::now();
	duration<double,std::micro>runtime_double=end-begin;
	cout << "\nThe time taken is : " << runtime_double.count() << " microseconds." << endl;
	return 0;
}



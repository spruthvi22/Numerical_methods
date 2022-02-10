# Program to find the nth Fibonacci number and find the time taken to do so

import time

def fib(n) :
    # Finds the nth Fibonacci number using the recurrence relation
    f1,f2,f3=0.0,1.0,0.0;
    if n==1 : return f1
    if n==2 : return f2
    for i in range(3,n+1) :
        f3=f1+f2
        f1,f2=f2,f3
    return f3

def main() :
    # Calls fib(n) to get the nth Fibonacci number and uses the time library to record the time taken in said function call. Both are then output to console.
    n=int(input("Enter value of n : "))
    begin=time.time()
    print("\nThe required Fibonacci number is :", fib(n))
    end=time.time()
    print("\nThe take for execution is :", ((end-begin)*10**6), "microseconds.")

if __name__=="__main__" :
    main()

# Program to find the largest element of a list

import random as rn

def large(arr,n) :
    # Iterates over an array to find the largest element and returns it.
    m=arr[0];
    for i in range(1,n) :
        if(arr[i]>m) :
            m=arr[i]
    return m

def main() :
    # Creates a 15 element array of random positive integers less than 20 and passes it to large(). Displays the result of this call as well.
    size=15
    arr=[rn.randint(0,20) for i in range(size)]
    print("The randomly generated array is : ")
    print(arr[0], end='')
    for i in range(1,size) : print(",", arr[i], end='')
    print("\n\nThe largest value in the array is :", large(arr,size))

if __name__=="__main__" :
    main()

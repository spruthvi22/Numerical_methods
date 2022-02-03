# Program to find the largest n elements of a list

import random as rn

def nlarge(arr,s,n) :
    # Implements a partial selection sort in descending order so that the n largest elements become the first n elements of the input list. Sorting is done inplace so no return required
    for i in range(n) :
        index=i;
        for j in range(i+1,s) :
            if(arr[j]>arr[index]) : arr[j],arr[index]=arr[index],arr[j]

def main() :
    # Creates a 15 element list of random positive integers less than 20  and passes it to nlarge(). Displays the result of this call as well.
    size=15
    arr=[rn.randint(0,20) for i in range(size)]
    print("The randomly generated array is : ")
    print(arr[0], end='')
    for i in range(1,size) : print(",", arr[i], end='')
    n=int(input("\n\nEnter the number of largest values required : "))
    nlarge(arr,size,n)
    print("\nThe",n,"largest values in the array in order are :",arr[0],end='')
    for i in range(1,n) : print(",", arr[i], end='')
    print()

if __name__=="__main__" :
    main()

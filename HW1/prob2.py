array=[50,24,90,76,54,1,9,87,100,12,89,900,45,780,899,901]

def sorting(arr,n):

      temp=arr[0]
      sort=arr


      for i in range(n):
            if array[i] >= temp:
                 temp=array[i]
        
            elif array[i] < temp:
                 temp=temp
      print(temp)
n=len(array)
sorting(array,n)


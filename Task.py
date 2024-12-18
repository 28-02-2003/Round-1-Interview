def array_rotate(arr,k):
    n=len(arr)
    k=k%n
    rotated=[0]*n
    for i in range(k):
        rotated[i]=arr[n-k+i]
    for i in range(n-k):
        rotated[k+i]=arr[i]
    return rotated
array=[1,2,3,4,5]
k=2
result=array_rotate(array,k)
print("Rotated Array is:",result)

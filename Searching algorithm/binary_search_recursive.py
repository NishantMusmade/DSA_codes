def binarySearch_Recursive(a,low,high,x):
    if low<=high:
        mid = (low+high)//2
        if x==a[mid]:
            return mid
        elif x < a[mid]:
            return binarySearch_Recursive(a,low,mid-1,x)
        else:
            return binarySearch_Recursive(a,mid+1,high,x)
    else:
        return -1
    


a = [1,2,3,4,67,78,89,90,102,304]
x = 89
index = binarySearch_Recursive(a,0,len(a)-1,x)

if index == -1:
    print('Element not found...!')
else:
    print(f'Element found at index {index}')
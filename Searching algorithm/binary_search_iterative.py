# Binary search using iterative approach

def binarySearch_Iteratie(a,n,x):
    if n!= 0:
        low = 0
        high = n-1
        
        while low<=high:
            mid = int(((low+high)/2))
            if x < a[mid]:
                high = mid-1
            elif x > a[mid]:
                low = mid + 1
            else:
                return mid 
    return -1


a = [1,2,3,4,67,78,89,90,102,304]
x = -1
index = binarySearch_Iteratie(a,len(a),x)

if index == -1:
    print('Element not found...!')
else:
    print(f'Element found at index {index}')

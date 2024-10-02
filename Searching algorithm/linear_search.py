def linearSearch(a,n,x):
    for i in range(n):
        if a[i] == x:
            return i
    # if element not found
    return -1

a = [1,2,3,4,90,89,32,21,1023]
x = 1
index = linearSearch(a,len(a),x)

if index == -1:
    print('Element not found...!')
else:
    print(f'Element found at index {index}')
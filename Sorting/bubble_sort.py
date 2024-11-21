def bubble_sort(a):
    for i in range(len(a)):
        swapped = 0
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                swapped = 1
        
        if swapped == 0:
            break
    
    return a

arr = [12,15,4,25,6,2]
print(bubble_sort(arr))
            



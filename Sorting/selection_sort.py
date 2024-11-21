def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
    
    return arr


arr = [4,2,1,6,7,5,6]
print(selection_sort(arr))
        

import sys
L = []

for i in range(1,100):
    print(i,sys.getsizeof(L))
    L.append(i)


#you will notice that the size of list is increasing if required in following manner
#first - more 4 bytes are allocated
#second - more 8 bytes are allocated
#third - more 12 bytes are allocated
#fourth - more 16 bytes are allocated


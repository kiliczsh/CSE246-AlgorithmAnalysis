import sys
import time
import numpy as np
def insertionSort(alist,k): #a list is an array , k is the index of wanted element
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position-1
        alist[position] = currentvalue
    return alist[k-1]

count=0
for input_size in range(1000,10001,1000):
    normal_array=np.random.random_integers(0,10000,size=(input_size))
    best_case=normal_array.copy()
    insertionSort(best_case,1)
    temp=best_case
    worst_case=list(reversed(temp)).copy()

    for array in [best_case,normal_array,worst_case]:
        start_time=time.time()
        kthElement=insertionSort(array,9)
        end_time=time.time()
        if count==0:
            print("Best case: %f"%(end_time-start_time),end="   ")
        elif count==1:
            print("Normal array: %f"%(end_time-start_time),end="   ")
        else:
            print("Worst case: %f"%(end_time-start_time))
        count+=1
        count=count%3
def insertionSort(alist,k):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position-1
        alist[position] = currentvalue
    return alist[k-1]

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
kthNum = insertionSort(alist,1) # 1-to-n
print(kthNum)


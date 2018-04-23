def merge_sort(lst,index):
    def kThElement(list,k):
        return list[k-1]


    def mergeSort(alist):
        if len(alist) > 1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            mergeSort(lefthalf)
            mergeSort(righthalf)

            lefthalfTest=lefthalf.copy()
            righthalfTest=righthalf.copy()

            i = 0
            j = 0
            k = 0
            while i < len(lefthalfTest) and j < len(righthalfTest):
                if lefthalfTest[i] < righthalfTest[j]:
                    alist[k] = lefthalfTest[i]
                    i = i+1
                else:
                    alist[k] = righthalfTest[j]
                    j = j+1
                k = k+1
            while i < len(lefthalfTest):
                alist[k] = lefthalfTest[i]
                i = i+1
                k = k+1

            while j < len(righthalfTest):
                alist[k] = righthalfTest[j]
                j = j+1
                k = k+1
    
    mergeSort(lst)
    kThElement(lst,index)

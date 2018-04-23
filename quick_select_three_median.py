import random

def quick_select_three_median(items, item_index):
    item_index=item_index-1
    def three_median(lst):
        lnt=len(lst)
        halflnt=lnt//2
        three=[[lst[0],0],[lst[halflnt],halflnt],[lst[lnt-1],lnt-1]]
        for i in range(len(three)-1,-1,-1):
            for j in range(i):
                if three[j][0]>three[j+1][0]:
                    three[j],three[j+1]=three[j+1],three[j]
        return three[1][1]

    def select(lst, l, r, index):
        # base case
        if r == l:
            return lst[l]
        median_index=three_median(items,l,r)

        lst[0],lst[median_index]=lst[median_index],lst[0]

        return partition(lst,l,r,index)

    def partition(lst,l,r,index):
        i = l
        for j in range(l, r):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        # move pivot to correct location
        lst[i], lst[l] = lst[l], lst[i]
        # recursively partition one side only
        if index == i:
            return lst[i]
        elif index < i:
            return select(lst, l, i-1, index)
        else:
            return select(lst, i+1, r, index)
    
    def select_test(lst,index,pivot):
        while len(lst)!=1:
            median_index=three_median(lst)
            lst[0],lst[median_index]=lst[median_index],lst[0]
            lst,index=partition_test(lst,index,lst[0])
        return lst[0]
    def partition_test(lst,index,pivot):
        lnt=len(lst)
        if(lnt==1): return lst[0]
        i=1
        j=lnt-1
        while i<j:
            while True:
                i+=1
                if lst[i]>=pivot:
                    break;
            while True:
                j-=1
                if lst[j]<=pivot:
                    break;
            lst[i],lst[j]=lst[j],lst[i]
        lst[i],lst[j]=lst[j],lst[i]
        lst[0],lst[j]=lst[j],lst[0]
        if j==index:
            index=index-j-1
            return [lst[j]],index
        elif j>index:
            index=index-j-1
            return lst[0:j],index
        else:
            index=index-j-1
            return lst[j+1:lnt],index
    if items is None or len(items) < 1:
        return None
    if item_index < 0 or item_index > len(items) - 1:
        raise IndexError()
    return select_test(items,item_index,items)
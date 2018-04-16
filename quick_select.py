import random
def quickselect(items, item_index):
    def select(lst, l, r, index):
        # base case
        if r == l:
            return lst[l]
        # choose random pivot
        pivot_index = random.randint(l, r)
        print("-----")
        print(pivot_index)
        print("-----")
        # move pivot to beginning of list
        lst[l], lst[pivot_index] = lst[pivot_index], lst[l]
        # partition
        i = l
        for j in range(l+1, r+1):
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
    if items is None or len(items) < 1:
        return None
    if item_index < 0 or item_index > len(items) - 1:
        raise IndexError()
    return select(items, 0, len(items) - 1, item_index)


a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
for i in range(0, len(a)):
    print("*")
    print(quickselect(a, i))    
    print("*")


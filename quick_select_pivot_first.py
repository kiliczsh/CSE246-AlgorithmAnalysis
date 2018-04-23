import random
def quick_select_pivot_first(items, item_index):
    item_index=item_index-1
    def select(lst, l, r, index):
        # base case
        if r == l:
            return lst[l]

        return partition(lst,l,r,index)

    def partition(lst,l,r,index):
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

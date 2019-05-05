def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)
    
def quickSortHelper(alist, first, last):
    if first < last:
        p = partition(alist, first, last)
        quickSortHelper(alist, first, p-1)
        quickSortHelper(alist, p+1, last)
    
def partition(alist, first, last):
    pivot = alist[last]    # 主元素
    left = first - 1    # 指向小于等于主元的最后一个
    right = first    # 指向大于主元的第一个
    while right <= last:
        if alist[right] <= pivot:    # 一旦小于等于主元，left加1，并交换当前right元素到left+1的位置
            left = left + 1
            alist[right], alist[left] = alist[left], alist[right]
        right += 1
#        print alist, left, right
    return left

if __name__ == "__main__":
    alist = [9,3,8,10,4,6,7]
    alist = [5,4,3,2,1]
    quickSort(alist)
    print alist

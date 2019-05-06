'''
给定一个升序数组alist和一个目标值target，用二分查找搜索，存在target，返回target的下标，否则返回-1
'''
def search(alist, target):
    if len(alist) == 1:
        if alist[0] == target:
            return 0
    first = 0
    last = len(alist) - 1
    while first <= last:
        mid = (first + last) //2
        if alist[mid] == target:
            return mid
        elif alist[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return -1

if __name__ == '__main__':
    alist = [2]
    target = 0
    print search(alist, target), 
#    print alist.index(target)

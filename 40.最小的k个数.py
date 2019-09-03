# 解法一，通过了牛客，利用快排的partition函数，复杂度O（n）

import random

def partition(lst, s, e):
    pivot = random.randint(s,e)
    p = lst[pivot]
    lst[e], lst[pivot] = lst[pivot], lst[e]
    small = s-1
    
    for i in range(s,e):
        if lst[i]<p:
            small += 1
            lst[i], lst[small] = lst[small], lst[i]

    small += 1
    lst[e], lst[small] = lst[small], p

    return small
    
def quicksort(tinput, s, e):
    idx = partition(tinput, s, e)
    if idx>s:
        quicksort(tinput, s, idx-1)
    if idx<e:
        quicksort(tinput, idx+1, e)
        
    return tinput
    

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        out = []
        if k>len(tinput):
            return out
        s = 0
        e = len(tinput)-1
        idx = partition(tinput, s, e)
        while(idx!=k-1):
            if idx > k-1:
                e = idx-1
                idx = partition(tinput, s, e)
            else:
                s = idx+1
                idx = partition(tinput, s, e)

        for i in range(k):
            out.append(tinput[i])
        return quicksort(out, 0, len(out)-1)

# 解法二，通过了牛客网，时间复杂度O（nlogk）,适合海量数据。
import heapq
class Solution:
    def GetLeastNumbers_Solution(self,arr, k):
        res = []
        if k>len(arr):
            return res
        max_heap = []
        for x in arr:
            heapq.heappush(max_heap, -x)
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        for x in max_heap:
            res.append(-x)
        return sorted(res)
        

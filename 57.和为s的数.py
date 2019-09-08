# 和为s的两个数字
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        small = 0
        big = len(array)-1
        if len(array)<2:
            return []
        while small < big:
            cur_sum = array[small]+array[big]
            if cur_sum == tsum:
                return [array[small],array[big]]
            while cur_sum < tsum and small<big:
                small +=1
                cur_sum = array[small]+array[big]
                if cur_sum == tsum:
                    return [array[small],array[big]]
            big -= 1
            
        return []

# 和为s的连续正数序列
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        if tsum<3:
            return res
        small = 1
        big = 2
        cur_sum = small+ big
        mid = (tsum+1)/2
        print mid
        while small < mid:
            if cur_sum == tsum:
                res.append([i for i in range(small, big+1)]) 
            while cur_sum > tsum and small<mid:
                cur_sum -= small
                small += 1
                if cur_sum == tsum:
                    res.append([i for i in range(small, big+1)])
            big += 1
            cur_sum += big
        return res

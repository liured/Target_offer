# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        curSum = None
        maxSum = None
        for item in array:
            if curSum == None:
                curSum = item
                maxSum = curSum
                print maxSum,
            else:
                if (curSum) > 0:  # 判断前面的加和是大于0还是小于0，大于0则加，小于0则抛弃前面的和，赋值当前值。
                    curSum = curSum + item
                else:
                    curSum = item
                maxSum = max(maxSum, curSum)
                print maxSum,
                
        return maxSum
        
        
# 解法二，使用动态规划方程。
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        f = []
        for i in range(len(array)):
            if i==0:
                f.append(array[i])
            else:
                f.append(array[i]+max(f[-1], 0)) # 利用动态规划，f(n) = array[n] + max(f(n-1), 0)
        return max(f)

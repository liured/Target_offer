class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        # 求从小到大排序的第index个丑数
        if index == 0:
            return 0
        res = [0] * index
        res[0] = 1
        idx2 = 0    # 乘以2的倍数的下标
        idx3 = 0    # 乘以3的倍数的下标
        idx5 = 0    # 乘以5的倍数的下标
        idx = 1
        while idx < index:
            res[idx] = min(res[idx2]*2, res[idx3]*3, res[idx5]*5)    # 各下标值乘以相应倍数，取最小则为下一个丑数。
            
            while res[idx2]*2 <= res[idx]:    # 更新乘以*倍数的下标
                idx2 += 1
            while res[idx3]*3 <= res[idx]:
                idx3 += 1
            while res[idx5]*5 <= res[idx]:
                idx5 += 1
            idx += 1
        return res[idx-1]

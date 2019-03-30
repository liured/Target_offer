# -*- coding:utf-8 -*-
'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        chou_number = []
        chou_number.append(1)
        cur_idx = 1    #目前有几个丑数了
        p2 = 0    #下标指向，这个数的2倍会比当前最大丑数大的下标
        p3 = 0
        p5 = 0
        while(cur_idx < index):
            m = min(chou_number[p2]*2, chou_number[p3]*3, chou_number[p5]*5)    #把当前2，3，5倍数最下的数保留。
            chou_number.append(m)
            while(chou_number[p2]*2 <= chou_number[-1]):
                p2 += 1
            while(chou_number[p3]*3 <= chou_number[-1]):
                p3 += 1
            while(chou_number[p5]*5 <= chou_number[-1]):
                p5 += 1
            cur_idx += 1
        return chou_number[-1]
    
if __name__ == "__main__":
    idx = raw_input()
    idx = int(idx)
    GetUglyNumber_Solution(idx)

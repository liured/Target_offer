# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        chou_number = []
        chou_number.append(1)
        cur_idx = 1
        p2 = 0
        p3 = 0
        p5 = 0
        while(cur_idx < index):
            m = min(chou_number[p2]*2, chou_number[p3]*3, chou_number[p5]*5)
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

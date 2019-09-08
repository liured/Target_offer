# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        s = s[::-1]
        s = list(s)
        print s
        cur_s = ""
        res_s = []
        i = -1
        for i in range(len(s)):
            if s[i]==" ":
                ccc = cur_s[::-1]
                res_s.append(ccc)
                cur_s = ""
            else:
                cur_s += s[i]
        print i,"".join(cur_s)[::-1]
        res_s.append("".join(cur_s)[::-1])
        return " ".join(res_s)

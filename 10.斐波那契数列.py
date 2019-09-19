# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        f0 = 0
        f1 = 1
        if n==0:
            return 0
        if n==1:
            return 1
        i = 2
        while i<=n:
            f2 = f0 + f1
            f0 = f1
            f1 = f2
            i += 1
        return f2
        
import sys
# 递归的方法
def Fibonacci(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)
    
# 循环的方法
def Fibonacci2(n):
    f0 = 0
    f1 = 1
    if n==0:
        return f0
    if n==1:
        return f1
    i = 2
    while i<=n:
        f2 = f0 + f1
        f0 = f1
        f1 = f2
        i += 1
    return f2
    
if __name__ == "__main__":
    line = sys.stdin.readline().strip()
#    val = map(int, line.split())
    n = int(line)
    
    print Fibonacci(n)
    print Fibonacci2(n)

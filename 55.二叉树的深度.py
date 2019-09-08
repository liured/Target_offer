# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 二叉树的深度，用递归求解
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot==None:
            return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))+1
        
        
# 判断是否为平衡二叉树

class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return self.depth(pRoot) != -1
    def depth(self, pRoot):
        if pRoot==None:
            return 0
        left = self.depth(pRoot.left)
        if left == -1:
            return -1
        right = self.depth(pRoot.right)
        if right == -1:
            return -1
        if abs(left-right)<2:
            return max(left, right) + 1
        else:
            return -1

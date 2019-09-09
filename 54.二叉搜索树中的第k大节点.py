'''
首先利用中序遍历，得到升序排序的节点列表。然后取列表中的第k-1个节点，即为第k大节点。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if k<=0:
            return None
        arr = []
        self.knode(pRoot, arr)
        if len(arr)<k:
            return None
        return arr[k-1]
    def knode(self, pRoot, res):
        if pRoot==None:
            return 
        if pRoot.left:
            self.knode(pRoot.left, res)
        res.append(pRoot)
        if pRoot.right:
            self.knode(pRoot.right, res)
            
#参考另一种方法
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if k<=0:
            return None
        _, value = self.knode(pRoot,k)
        return value

    def knode(self, pRoot, k):
        if pRoot==None:
            return k,None
        k,value = self.knode(pRoot.left, k)
        if value:
            return k, value
        if k==1:
            return k,pRoot
        k = k-1
        return self.knode(pRoot.right, k)

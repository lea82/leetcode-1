# -*- coding: utf-8 -*-
"""
108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        http://www.cnblogs.com/zuoyuan/p/3722103.html
        解题思路：由于要求二叉查找树是平衡的。
        所以我们可以选在数组的中间那个数当树根root，
        然后这个数左边的数组为左子树，右边的数组为右子树，
        分别递归产生左右子树就可以了。

        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        root = TreeNode(nums[len(nums) / 2])
        # left of mid is left tree
        root.left = self.sortedArrayToBST(nums[:len(nums) / 2])
        # right of mid is right tree
        root.right = self.sortedArrayToBST(nums[len(nums) / 2 + 1:])
        return root

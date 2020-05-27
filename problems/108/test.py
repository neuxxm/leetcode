# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#11:47-11:50
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        a = nums
        if len(a) == 0:
            return None
        mid = len(a) / 2
        root = TreeNode(a[mid])
        root.left = self.sortedArrayToBST(a[:mid])
        root.right = self.sortedArrayToBST(a[mid+1:])
        return root

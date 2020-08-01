# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#18:05-18:07
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        a = nums
        n = len(a)
        if n == 0:
            return None
        ix = n / 2
        root = TreeNode(a[ix])
        root.left = self.sortedArrayToBST(a[:ix]) 
        root.right = self.sortedArrayToBST(a[ix+1:])
        return root

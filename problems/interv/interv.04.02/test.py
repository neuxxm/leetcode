# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#11:57-11:58
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        a = nums
        if len(a) == 0:
            return None
        n = len(a)
        mid = n/2
        r = TreeNode(a[mid])
        r.left = self.sortedArrayToBST(a[:mid])
        r.right = self.sortedArrayToBST(a[mid+1:])
        return r

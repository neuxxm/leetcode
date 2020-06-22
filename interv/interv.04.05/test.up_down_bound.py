# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#16:54
def is_bst(x, l, r):
	if x.val < l or x.val > r:
        return False
    if x.left:
        return is_bst(x.left, l, min(x.val, r))
    if x.right:
        return is_bst(x.right, max(l, x.val), r)
    return True
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
		if root == None:
			return True
		return is_bst(root, float('-inf'), float('inf'))

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#16:27-16:38
def calc_sum(x):
    r = x.val
    if x.left:
        r += calc_sum(x.left)
    if x.right:
        r += calc_sum(x.right)
    return r
def visit(x, r):
    left_sum = 0
    right_sum = 0
    if x.left:
        left_sum = calc_sum(x.left)
        visit(x.left, r)
    if x.right:
        right_sum = calc_sum(x.right)
        visit(x.right, r)
    r[0] += abs(left_sum - right_sum)
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        r = [0]
        visit(root, r)
        return r[0]

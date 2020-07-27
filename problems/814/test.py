# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#11:22-11:31
def check(x):
    if x == None:
        return True
    if x.val != 0:
        return False
    return check(x.left) and check(x.right)
def f(x):
    if x == None:
        return
    f(x.left)
    f(x.right)
    #deal x
    if check(x.left):
        x.left = None
    if check(x.right):
        x.right = None
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        f(root)
        return root

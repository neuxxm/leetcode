# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#13:25fail
def f(x, path, z, q):
    if x.left:
        q.append(x.left)
    if x.right:
        q.append(x.right)
    if len(q) == 0:
        z.append(path)
        return
    for i,t in enumerate(q):
        q2 = q[:i] + q[i+1:]
        f(t, path + [t.val], z, q2)
class Solution(object):
    def BSTSequences(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return [[]]
        z = []
        q = []
        f(root, [root.val], z, q)
        return z

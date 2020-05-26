# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#12:34-12:50
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        q = []
        q.append(root)
        cnt = 0
        while len(q) > 0:
            t = q.pop(0)
            if t == None:
                break
            q.append(t.left)
            q.append(t.right)
        b = True
        for i in q:
            if i:
                b = False
                break
        return b

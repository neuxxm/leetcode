# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#19:49-19:53
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        q = []
        q2 = []
        q.append(root.left)
        q2.append(root.right)
        while len(q) > 0 and len(q2) > 0:
            t = q.pop()
            t2 = q2.pop()
            if t == None and t2 == None:
                continue
            if t == None and t2 != None:
                return False
            if t != None and t2 == None:
                return False
            if t.val != t2.val:
                return False
            q.append(t.left)
            q.append(t.right)
            q2.append(t2.right)
            q2.append(t2.left)
        return len(q) == 0 and len(q2) == 0

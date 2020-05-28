# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#11:50-11:52
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        q = []
        q.append(root)
        r = []
        while len(q) > 0:
            t = q.pop(0)
            r.append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        return r

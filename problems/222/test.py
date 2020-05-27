# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        q = []
        q.append(root)
        cnt = 0
        while len(q) > 0:
            t = q.pop(0)
            cnt += 1
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        return cnt

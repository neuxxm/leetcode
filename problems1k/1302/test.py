# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#18:48-18:49
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        q = [root]
        z = 0
        while q:
            xs = []
            while q:
                xs.append(q.pop(0))
            r = 0
            for x in xs:
                r += x.val
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            z = r
        return z

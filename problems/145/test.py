# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#15:18fail
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q = []
        p = root
        r = []
        last = None
        while p or len(q) > 0:
            if p:
                q.append(p)
                p = p.left
            else:
                p = q[len(q) - 1]
                if p.right and p.right != last:
                    p = p.right
                else:
                    r.append(p.val)
                    q.pop()
                    last = p
                    p = None
        return r

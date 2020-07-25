# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#12:59-13:04
#  1
# 2 3
#4 5
#[3, 1, Non, 5, 2, Non, 4, Non]
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        q = []
        q.append(root)
        b = False
        while q:
            x = q.pop()
            if x:
                if x.right:
                    q.append(x.right)
                q.append(x)
                q.append(None)
                if x.left:
                    q.append(x.left)
            else:
                x = q.pop()
                if b:
                    return x
                if x == p:
                    b = True
        return None

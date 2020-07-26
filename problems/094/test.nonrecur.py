# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#16:11-16:16
#  1 
# 2 3
#4 5
#[3,1,non,5,2,non,4,non]
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        q = []
        q.append(root)
        r = []
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
                r.append(x.val)
        return r

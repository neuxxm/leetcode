# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
        while len(q) > 0:
            t = q.pop()
            if t:
                if t.right:
                    q.append(t.right)
                q.append(t)
                q.append(None)
                if t.left:
                    q.append(t.left)
            else:
                t = q.pop()
                r.append(t.val)
        return r

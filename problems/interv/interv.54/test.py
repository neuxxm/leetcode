# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.right = None
#         self.left = None
#13:40-13:53
class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cur = root
        cnt = 0
        r = -1
        while cur:
            if cur.right:
                p = cur.right
                while p.left and p.left != cur:
                    p = p.left
                if p.left:
                    cnt += 1
                    if cnt == k:
                        return cur.val
                    p = None
                    cur = cur.left
                else:
                    p.left = cur
                    cur = cur.right
            else:
                cnt += 1
                if cnt == k:
                    return cur.val
                cur = cur.left
        return r

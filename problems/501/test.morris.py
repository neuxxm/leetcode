# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#18:18-18:57
def f(x, last, cnt, ma, mak):
    if last != None:
        if x == last:
            cnt += 1
        else:
            last = x
            cnt = 1
    else:
        last = x
        cnt = 1
    if cnt > ma:
        ma = cnt
        mak = [x]
    elif cnt == ma:
        mak.append(x)
    return last, cnt, ma, mak
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur = root
        last = None
        cnt = 0
        ma = 0
        mak = []
        while cur:
            if cur.left:
                p = cur.left
                while p.right and p.right != cur:
                    p = p.right
                if p.right:
                    last, cnt, ma, mak = f(cur.val, last, cnt, ma, mak)
                    p.right = None
                    cur = cur.right
                else:
                    p.right = cur
                    cur = cur.left
            else:
                last, cnt, ma, mak = f(cur.val, last, cnt, ma, mak)
                cur = cur.right
        return mak

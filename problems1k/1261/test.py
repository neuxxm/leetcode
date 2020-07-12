# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#20:43-23:00
def visit(x):
    if x.left:
        x.left.val = x.val*2+1
        visit(x.left)
    if x.right:
        x.right.val = x.val*2+2
        visit(x.right)
def f(x, r, ix, n):
    if ix >= n:
        return False
    #print ix, r[ix]
    if ix == n-1:
        return True
    is_left = (r[ix+1]&1) != 0
    if is_left:
        if x.left == None:
            return False
        if f(x.left, r, ix+1, n):
            return True
    else:
        if x.right == None:
            return False
        if f(x.right, r, ix+1, n):
            return True
    return False
class FindElements(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if root == None:
            return
        visit(root)
        self.root = root

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        y = target
        r = []
        r.append(y)
        while True:
            if y&1:
                t = (y-1)/2
            else:
                t = (y-2)/2
            if t < 0:
                break
            r.append(t)
            y = t
        return f(self.root, r[::-1], 0, len(r))

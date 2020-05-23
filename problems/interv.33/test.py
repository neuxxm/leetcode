#11:07-11:23
def gt(a, x):
    n = len(a)
    for i in xrange(n):
        if a[i] < x:
            return False
    return True
def lt(a, x):
    n = len(a)
    for i in xrange(n):
        if a[i] > x:
            return False
    return True
class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        a = postorder
        n = len(a)
        if n == 0:
            return True
        if n == 1:
            return True
        r = a[n-1]
        ix = -1
        for i in xrange(n-1, -1, -1):
            if a[i] < a[n-1]:
                ix = i
                break
        if ix == -1:
            return self.verifyPostorder(a[:-1]) if gt(a[:-1], a[n-1]) else False
        elif ix == n-2:
            return self.verifyPostorder(a[:-1]) if lt(a[:-1], a[n-1]) else False
        else:
            b = self.verifyPostorder(a[:ix+1]) if lt(a[:ix+1], a[n-1]) else False
            if not b:
                return False
            return self.verifyPostorder(a[ix+1:-1]) if gt(a[ix+1:-1], a[n-1]) else False

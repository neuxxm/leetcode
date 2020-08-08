#19:09-19:13
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
        root = a[n-1]
        i = 0
        while i < n-1:
            if a[i] > root:
                break
            i += 1
        for j in xrange(i, n-1):
            if a[j] < root:
                return False
        return self.verifyPostorder(a[:i]) and self.verifyPostorder(a[i:n-1])

#1:45-1:46
class Solution(object):
    def isUnique(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        a = sorted(astr)
        n = len(a)
        for i in xrange(1, n):
            if a[i] == a[i-1]:
                return False
        return True

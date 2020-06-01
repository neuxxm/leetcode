class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        a = target
        b = arr
        n = len(a)
        m = len(b)
        if n != m:
            return False
        a.sort()
        b.sort()
        for i in xrange(len(a)):
            if a[i] != b[i]:
                return False
        return True

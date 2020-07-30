#19:42fail
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        n = len(a)
        m = len(b)
        if n != m:
            return max(n, m)
        else:
            if a == b:
                return -1
            return n

#12:36-12:37
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        n = len(s)
        r = [0] * n
        for i in xrange(n):
            r[indices[i]] = s[i]
        return ''.join(r)

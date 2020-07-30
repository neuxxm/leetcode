#16:15-16:17
from collections import defaultdict
def f(s):
    cnt = defaultdict(lambda:0)
    for c in s:
        cnt[c] += 1
    return cnt
class Solution(object):
    def CheckPermutation(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        c = f(s1)
        c2 = f(s2)
        if len(c) != len(c2):
            return False
        for k,v in c.items():
            if k not in c2:
                return False
            if v != c2[k]:
                return False
        return True

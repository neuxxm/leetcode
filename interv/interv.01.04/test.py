#23:31-23:33
from collections import defaultdict
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #a
        #aa
        #aba
        #abba
        cnt = defaultdict(lambda:0)
        for c in s:
            cnt[c] += 1
        r = 0
        for v in cnt.values():
            if v&1:
                r += 1
        return r < 2

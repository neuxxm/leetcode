#23:04-23:07
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = {}
        for c in s:
            if c in cnt:
                cnt[c] += 1
            else:
                cnt[c] = 1
        z = 0
        b = False
        for v in cnt.values():
            if v&1:
                z += (v-1)
                b = True
            else:
                z += v
        if b:
            z += 1
        return z

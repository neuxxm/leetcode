#13:10-13:20
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = {}
        for c in s:
            count[c] = 0
        l = 0
        r = 0
        z = 0
        while r < n:
            while r < n:
                c = s[r]
                if count[c] == 0:
                    count[c] = 1
                    r += 1
                else:
                    break
            t = r-l
            #print l, r
            if t > z:
                z = t
            while l < n:
                c = s[l]
                l += 1
                count[c] -= 1
                if count[c] == 0:
                    break
        return z

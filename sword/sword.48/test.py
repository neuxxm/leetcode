#19:30-19:46
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = {}
        for c in s:
            cnt[c] = 0
        n = len(s)
        l = 0
        r = 0
        ans = ''
        while r < n:
            #print l, r
            while r < n:
                c = s[r]
                if cnt[c] == 1:
                    break
                cnt[c] += 1
                r += 1
            t = s[l:r]
            if len(t) > len(ans):
                ans = t
            while l < r:
                c = s[l]
                b = cnt[c] == 1
                l += 1
                cnt[c] -= 1
                if b:
                    break
        return len(ans)

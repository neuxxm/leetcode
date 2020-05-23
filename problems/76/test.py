#22:25-22:32fail
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = {}
        cnt = {}
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
                cnt[c] = 0
        m = len(need)
        n = len(s)
        l = 0
        r = 0
        valid = 0
        mi = n + 10
        ans = ''
        while r < n:
            c = s[r]
            if c in need:
                cnt[c] += 1
                if cnt[c] == need[c]:
                    valid += 1
            r += 1
            while valid == m:
                t = r-l
                if t < mi:
                    mi = t
                    ans = s[l:r]
                c = s[l]
                if c in need:
                    if cnt[c] == need[c]:
                        valid -= 1
                    cnt[c] -= 1
                l += 1
        return ans

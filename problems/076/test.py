#6.25 15:49-16:02
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = {}
        cnt = {}
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
            cnt[c] = 0
        m = len(cnt)
        n = len(s)
        l = 0
        r = 0
        z = 0
        ans = ''
        ans_len = n + 1
        while r < n:
            while r < n:
                c = s[r]
                r += 1
                if c in need:
                    cnt[c] += 1
                    if cnt[c] == need[c]:
                        z += 1
                        if z == m:
                            break
            while z == m:
                c = s[l]
                t = r - l
                if t < ans_len:
                    ans = s[l:r]
                    ans_len = t
                l += 1
                if c in need:
                    cnt[c] -= 1
                    if cnt[c] < need[c]:
                        z -= 1
                        break
        return ans if ans_len != n+1 else ''

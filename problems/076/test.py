#15:51-16:20
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = {}
        cnt = {}
        valid = 0
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
                cnt[c] = 0
        need_len = len(need)
        n = len(s)
        l = 0
        r = 0
        z = n+1
        zs = ''
        while True:
            while r < n:
                c = s[r]
                r += 1
                if c in need:
                    cnt[c] += 1
                    if cnt[c] == need[c]:
                        valid += 1
                        if valid == need_len:
                            break
            if valid != need_len:
                break
            while l < n:
                c = s[l]
                l += 1
                if c in need:
                    if cnt[c] == need[c]:
                        cnt[c] -= 1
                        valid -= 1
                        break
                    else:
                        cnt[c] -= 1
            t = r-l+1
            if t < z:
                z = t
                zs = s[l-1:r]
        return zs

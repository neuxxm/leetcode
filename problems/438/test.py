#16:37-15:13fail
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        need = {}
        cnt = {}
        for c in p:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
                cnt[c] = 0
        need_len = len(need)
        n = len(s)
        l = 0
        r = 0
        valid = 0
        p_len = len(p)
        zs = []
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
                if r-l == p_len:
                    #print s[l:r], l
                    zs.append(l)
                l += 1
                if c in need:
                    if cnt[c] == need[c]:
                        cnt[c] -= 1
                        valid -= 1
                        break
                    else:
                        cnt[c] -= 1
        return zs

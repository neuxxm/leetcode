#17:38-17:45
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s = s2
        s1_len = len(s1)
        need = {}
        cnt = {}
        for c in s1:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
                cnt[c] = 0
        need_len = len(need)
        n = len(s)
        l = 0
        r = 0
        b = False
        valid = 0
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
                if r - l == s1_len:
                    return True
                l += 1
                if c in need:
                    if cnt[c] == need[c]:
                        cnt[c] -= 1
                        valid -= 1
                        break
                    else:
                        cnt[c] -= 1
        return False

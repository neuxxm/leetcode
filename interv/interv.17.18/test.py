#19:47-19:59
class Solution(object):
    def shortestSeq(self, big, small):
        """
        :type big: List[int]
        :type small: List[int]
        :rtype: List[int]
        """
        need = {}
        cnt = {}
        for t in small:
            if t in need:
                need[t] += 1
            else:
                need[t] = 1
                cnt[t] = 0
        y = len(need)
        l = 0
        r = 0
        n = len(big)
        s = big
        z = 0
        ans = []
        ans2 = []
        while r < n:
            # [l, r)
            while r < n:
                c = s[r]
                r += 1
                if c in need:
                    cnt[c] += 1
                    if cnt[c] == need[c]:
                        z += 1
                        if z == y:
                            break
            while z == y:
                t = r-l
                if len(ans) == 0:
                    ans = s[l:r]
                    ans2 = []
                    ans2.append(l)
                    ans2.append(r-1)
                elif t < len(ans):
                    ans = s[l:r]
                    ans2[0] = l
                    ans2[1] = r-1
                elif t == len(ans) and l < ans2[0]:
                    ans = s[l:r]
                    ans2[0] = l
                    ans2[1] = r-1
                c = s[l]
                l += 1
                if c in need:
                    if cnt[c] == need[c]:
                        cnt[c] -= 1
                        z -= 1
                        break
                    else:
                        cnt[c] -= 1
        return ans2

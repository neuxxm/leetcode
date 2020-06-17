#14:27AC
import bisect
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        n = len(hand)
        w = W
        if n%w != 0:
            return False
        a = sorted(hand)
        bit = [0] * n
        i = 0
        while i < n:
            start = a[i]
            map = {}
            for k in xrange(0, w):
                map[start+k] = 0
            up = start+w-1
            j = i
            cnt = 0
            b = False
            while j < n:
                if a[j] > up:
                    return False
                if bit[j] == 0:
                    if a[j] in map and map[a[j]] == 0:
                        bit[j] = 1
                        map[a[j]] = 1
                        cnt += 1
                        if cnt == w:
                            b = True
                            break
                j += 1
            if not b:
                return False
            t = i
            while t < n:
                if bit[t] == 0:
                    break
                else:
                    t += 1
            i = t
        return True

#13:52-14:05
def gcd(x, y):
    if x > y:
        if y == 0:
            return x
        return gcd(y, x%y)
    else:
        if x == 0:
            return y
        return gcd(x, y%x)
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        a = deck
        n = len(a)
        map = {}
        for t in a:
            if t in map:
                map[t] += 1
            else:
                map[t] = 1
        b = True
        r = 0
        for v in map.values():
            if b:
                b = False
                r = v
            else:
                r = gcd(r, v)
            if r < 2:
                return False
        return True

#17:07-17:22
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        xt = x
        l = 0
        while x > 0:
            x /= 10
            l += 1
        q = []
        z = 0
        mid = l / 2
        x = xt
        if (l&1) != 0:
            while x > 0:
                t = x%10
                if z == mid:
                    pass
                elif z < mid:
                    q.append(t)
                else:
                    t2 = q.pop()
                    if t != t2:
                        return False
                z += 1
                x /= 10
        else:
            while x > 0:
                t = x%10
                if z < mid:
                    q.append(t)
                else:
                    t2 = q.pop()
                    if t != t2:
                        return False
                z += 1
                x /= 10
        return True

#21:41-22:48
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        c5 = 0
        c10 = 0
        c20 = 0
        for t in bills:
            if t == 5:
                c5 += 1
            elif t == 10:
                if c5 > 0:
                    c5 -= 1
                else:
                    return False
                c10 += 1
            else:
                if c10 > 0:
                    c10 -= 1
                    if c5 > 0:
                        c5 -= 1
                    else:
                        return False
                    c20 += 1
                elif c5 > 0:
                    if c5 >= 3:
                        c5 -= 3
                    else:
                        return False
                    c20 += 1
                else:
                    return False
        return True

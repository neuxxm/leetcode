#12:40-12:47
class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        a = low&1
        b = high&1
        t = a*10 + b
        if t == 10 or t == 1:
            return (high-low-1) / 2 + 1
        elif t == 11:
            return (high-low-2) / 2 + 2
        else:
            return (high-low) / 2

#11:23-11:25
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        a = candies
        m = extraCandies
        ma = max(a)
        r = []
        for t in a:
            r.append(t+m >= ma)
        return r

#11:09-11:37
class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        map = {}
        list = []
        a = shorter
        b = longer
        for l in xrange(0, k+1):
            r = k-l
            t = a*l + b*r
            if t == 0:
                continue
            if t not in map:
                map[t] = 1
                list.append(t)
        return sorted(list)

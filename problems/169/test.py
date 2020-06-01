#00:03-00:05
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        z = n/2
        map = {}
        for t in a:
            if t in map:
                map[t] += 1
                if map[t] > z:
                    return t
            else:
                map[t] = 1
                if map[t] > z:
                    return t

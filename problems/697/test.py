#23:22-23:33
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        map1 = {}
        map2 = {}
        mv = 0
        for i,t in enumerate(nums):
            if t in map:
                map[t] += 1
                map2[t] = i
            else:
                map[t] = 1
                map1[t] = i
            if map[t] > mv:
                mv = map[t]
        n = len(nums)
        z = n+1
        for k,v in map.items():
            if v == mv:
                if k in map2:
                    t = map2[k]
                else:
                    t = map1[k]
                t -= map1[k]
                if t < z:
                    z = t
        return z+1

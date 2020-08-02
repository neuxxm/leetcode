from collections import defaultdict
class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m = 1000000007
        ma = 10000001
        c1 = defaultdict(lambda:0)
        c2 = defaultdict(lambda:0)
        map = defaultdict(lambda:0)
        a = nums1
        b = nums2
        for t in a:
            c1[t] = 1
            map[t] = 1
        c1[ma] = 1
        for t in b:
            c2[t] = 1
            map[t] = 1
        c2[ma] = 1
        map[ma] = 1
        x = 0
        y = 0
        z = 0
        for i in sorted(map.keys()):
            if c1[i]>0 and c2[i]>0:
                z += max(x,y)
                if i != ma:
                    z += i
                z %= m
                x = 0
                y = 0
            elif c1[i]>0:
                x += i
                #x %= m
            elif c2[i]>0:
                y += i
                #y %= m
        return z

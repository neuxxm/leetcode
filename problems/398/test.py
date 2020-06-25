#6.25 23:33-23:40
import random
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.a = nums
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        #k=1000, 1000/1001 sample, 1/1000 replace
        #1/1001 + 1000/1001*999/1000 = 1000/1001
        ans = 0
        i = 0
        for ix,t in enumerate(self.a):
            if t == target:
                i += 1
                r = random.randint(1, i)
                if r <= 1:
                    ans = ix
        return ans

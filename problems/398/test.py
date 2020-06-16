#23:27fail
import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.a = nums[:]
        self.n = len(nums)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        cnt = 0
        z = 0
        for i in xrange(self.n):
            if self.a[i] == target:
                cnt += 1
                #1000/1001 k/i 1/i
                t = random.randint(1, cnt)
                #1/1000 1/k 1
                if t <= 1:
                    z = i
        return z

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

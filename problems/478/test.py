#19:58-20:07
import random
def f(x):
    return x*x
class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.x = x_center
        self.y = y_center
        self.r = radius
    def randPoint(self):
        """
        :rtype: List[float]
        """
        x = self.x
        y = self.y
        r = self.r
        r2 = f(r)
        while True:
            x2 = random.uniform(x-r, x+r)
            y2 = random.uniform(y-r, y+r)
            if f(x-x2) + f(y-y2) <= r2:
                l = []
                l.append(x2)
                l.append(y2)
                return l
# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

#6.27 13:09fail
import random
def f(x):
    return x*x
class Solution(object):
    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.x = x_center
        self.y = y_center
        self.r = radius
    def randPoint(self):
        """
        :rtype: List[float]
        """
        r = self.r
        x = self.x
        y = self.y
        r2 = f(r)
        while True:
            x2 = random.uniform(x - r, x + r)
            y2 = random.uniform(y - r, y + r)
            if f(x2-x) + f(y2-y) <= r2:
                l = []
                l.append(x2)
                l.append(y2)
                return l

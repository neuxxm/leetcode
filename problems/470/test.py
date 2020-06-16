# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
#0:42fail
class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        #[0,1,2,3,4,5,6] * 7 + [1,2,3,4,5,6,7]
        #[0,7,14,21,28,35,42] + [1,2,3,4,5,6,7]
        while True:
            t = (rand7()-1) * 7 + rand7()
            if t <= 40:
                return t%10 + 1

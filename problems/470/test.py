# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
#13:13-13:21
class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            n = (rand7()-1) * 7 + rand7()
            if n <= 40:
                return n%10+1

#15:01-15:02
class Solution(object):
    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
        n = len(guess)
        r = 0
        for i in xrange(n):
            if guess[i] == answer[i]:
                r += 1
        return r

#17:20
def f(s, istr):
    buf = ''
    for c in s:
        n = ord(c) - ord('a')
        buf += istr[n]
    return buf
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
		istr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s1 = set()
		for w in words:
            s = f(w, istr)
            s1.add(s)
        return len(s)

#13:53AC
class WordsFrequency(object):

    def __init__(self, book):
        """
        :type book: List[str]
        """
        self.dict = {}
        dict = self.dict
        for t in book:
            if t in dict:
                dict[t] += 1
            else:
                dict[t] = 1

    def get(self, word):
        """
        :type word: str
        :rtype: int
        """
        dict = self.dict
        if word in dict:
            return dict[word]
        else:
            return 0

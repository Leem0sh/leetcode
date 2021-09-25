class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        tpls = [(word, int(word[-1])) for word in words]
        tpls = sorted(tpls, key=lambda x: x[1])
        list_of_words = [pair[0][:-1] for pair in tpls]
        return " ".join(list_of_words)


Solution().sortSentence("sentence4 a3 is2 This1")
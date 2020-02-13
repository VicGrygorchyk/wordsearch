"""A board of random words."""


class Board:

    def __init__(self, table):
        self.table = table

    def contains_word(self, word):
        """Returns a word if contains it."""
        word0 = self._search_by_row(word)
        word1 = self._search_by_col(word)
        word2 = self._search_by_diagonal(word)
        words = {word0, word1, word2}
        words_filtered = [word_ for word_ in words if word_]
        if words_filtered:
            return words_filtered.pop()  # assume all words are the same
        return None

    def _search_by_row(self, word):
        """Search a word and reversed word to hack reversed search"""
        for row in self.table:
            if word in row or "".join(reversed(word)) in row:
                return word
        return False

    def _search_by_col(self, word):
        for index in range(len(self.table[0])):
            column = "".join([word[index] for word in self.table])
            if word in column or "".join(reversed(word)) in column:
                return word
        return False

    def _search_by_diagonal(self, word):
        for index in range(len(self.table[0])):
            diagonal = ""
            for k in range(len(self.table)):
                diagonal = "".join([word[k] for word in self.table])
            if word in diagonal or "".join(reversed(word)) in diagonal:
                return word
        return False

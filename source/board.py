"""A board of random words."""


class Board:

    def __init__(self, table):
        self.table = table

    def contains_word(self, word):
        """Returns a word if contains it."""
        word = self._search_by_row(word)
        if word:
            return word

    def _search_by_row(self, word):
        """Search a word and reversed word to hack reversed search"""
        for row in self.table:
            if word in row or "".join(reversed(word)) in row:
                return word
        return False

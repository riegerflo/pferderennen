from itertools import product
from collections import Counter
from random import shuffle

NUMBERS = ["6", "7", "8", "9", "10", "U", "O", "K"]  # , "A"]
COLORS = ["S", "H", "G", "E"]

SYMBOLS = {"S": "@", "H": "<3", "G": "#", "E": "0"}


class Deck:
    """A deck of bavarian Schafkopf cards."""

    def __init__(self):
        self._deck = self._init_deck()
        self.shuffle()

    def shuffle(self):
        shuffle(self._deck)

    def draw(self):
        return self._deck.pop()

    def _init_deck(self):
        return list(product(NUMBERS, COLORS))

    def _introduce_bias(self):
        """Changes the probabilities for different horses."""
        cnt = Counter()
        for card in self._deck:
            if card[1] == "H" and cnt["H"] < 1:
                self._deck.remove(card)
                cnt["H"] += 1
            if card[1] == "G" and cnt["G"] < 2:
                self._deck.remove(card)
                cnt["G"] += 1
            if card[1] == "E" and cnt["E"] < 3:
                self._deck.remove(card)
                cnt["E"] += 1

    def __str__(self):
        return str(self._deck)


if __name__ == "__main__":
    deck = Deck()
    print(deck)
    print(deck.draw())
    print(deck)

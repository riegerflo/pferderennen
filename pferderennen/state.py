import abc
from collections import Counter

# from pferderennen.deck import Deck, COLORS
from pferderennen.deck import Deck, COLORS, SYMBOLS


class Context:
    _state = None

    def __init__(self, state: "State", print_game=False, bias=True):
        self._bias = bias
        self._print_game = print_game
        self._initialize()
        self.transition_to(state)

        self.victories = Counter()

    def _initialize(self):
        self._deck = Deck()

        if self._bias:
            self._deck._introduce_bias()

        self._current_card = None
        self._race_track = {c: 0 for c in COLORS}
        self._boost_track = None

    def transition_to(self, state):
        self._state = state
        self._state._context = self

    def move_horse(self):
        self._race_track[self._current_card[1]] += 1

        if self._print_game:
            self.print_game()

    def next(self):
        self._state.next()

    def print_game(self):
        print("--------------------------------------------")
        for c in COLORS:
            pos = self._race_track[c]
            s = pos * "---" + SYMBOLS[c]
            print(s)
        print("--------------------------------------------")


class State(abc.ABC):
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context: Context):
        self._context = context

    @abc.abstractmethod
    def next(self):
        ...


if __name__ == "__main__":
    print("Hello")

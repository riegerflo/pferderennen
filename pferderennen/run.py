"""Main module."""
import time

# from pferderennen.state import Context, State
from pferderennen.state import Context, State, Deck


class NewGame(State):
    """New game with shuffled deck."""

    def next(self):
        # print("A new game starts!")
        self.context._initialize()
        self.context._boost_track = [self.context._deck.draw() for i in range(4)]
        self.context._race_track = {c: 0 for c in self.context._race_track}
        self.context.transition_to(BeforeMove())


class BeforeMove(State):
    """Draws a new card to determine which horse moves next."""

    def next(self):
        # print("Rötörötörötörötödödööööööööööööö!")
        self.context._current_card = self.context._deck.draw()
        # print(f"Next card is {self.context._current_card}")
        self.context.move_horse()
        self.context.transition_to(AfterMove())


class AfterMove(State):
    """Checks if boost or winning condition is fullfilled and acts accordingly."""

    def next(self):
        if self.context._race_track[self.context._current_card[1]] == 5:
            # print(f"{self.context._current_card[1]} wins!")
            self.context.victories[self.context._current_card[1]] += 1
            self.context.transition_to(Finish())

        elif min(self.context._race_track.values()) >= (
            5 - len(self.context._boost_track)
        ):
            # print(f"Boost, boost, booooooooost!!!")
            self.context._current_card = self.context._boost_track.pop()
            # print(f"{self.context._current_card} gets the boost!")
            self.context.move_horse()
            self.context.transition_to(AfterMove())
        else:
            # print("Next round...")
            self.context.transition_to(BeforeMove())


class Finish(State):
    """Game is finished."""

    def next(self):
        # print(f"Current standing:/n {self.context.victories}")
        # time.sleep(1)
        # print("Resetting game...")
        self.context.transition_to(NewGame())


if __name__ == "__main__":
    game_state = NewGame()
    context = Context(game_state, print_game=False)

    history = []
    cnt = 0
    while True:
        context._state.next()
        # time.sleep(1)
        if isinstance(context._state, Finish):
            cnt += 1
            history.append(list(context.victories.values()))
        if cnt == 1000000:
            break
    print(context.victories)
    print(history)

    import matplotlib.pyplot as plt
    import numpy as np

    plt.figure()
    plt.plot(np.array(history))
    plt.show()

class InvalidGameState(Exception):
    pass


class Game:
    def __init__(self, initial_state):
        self._validate_initial_state(initial_state)
        self.state = [card for card in initial_state]

    def _validate_initial_state(self, initial_state):
        if not isinstance(initial_state, str):
            raise InvalidGameState("initial state was not a string")

        for card in initial_state:
            if card is not "0" and card is not "1":
                raise InvalidGameState("found card in initial state that was not a 0 or a 1")

    def take(self, index):
        if index < 0 or index >= len(self.state):
            return

        if self.state[index] is "." or self.state[index] is "0":
            return

        self.state[index] = "."
        self._flip(index + 1)
        self._flip(index - 1)

    def _flip(self, index):
        if index < 0 or index >= len(self.state) or self.state[index] is ".":
            return

        self.state[index] = "1" if self.state[index] is "0" else "0"

    def successful(self):
        return all(card is "." for card in self.state)

    def stuck(self):
        some_zeros = any(card is "0" for card in self.state)
        no_ones = all(card is not "1" for card in self.state)
        return some_zeros and no_ones

    def print(self):
        print("".join(self.state))

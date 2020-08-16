class Game:
    def __init__(self, initial_state):
        self.state = [card for card in initial_state]

    def get_number_of_ones(self):
        return self.state.count("1")

    def get_first_one(self):
        for i in range(len(self.state)):
            if self.state[i] is "1":
                return i

    def take(self, index):
        if index < 0 or index >= len(self.state):
            return

        if self.state[index] is "." or self.state[index] is "0":
            return

        self.state[index] = "."
        self.flip(index + 1)
        self.flip(index - 1)

    def flip(self, index):
        if index < 0 or index >= len(self.state) or self.state[index] is ".":
            return

        self.state[index] = "1" if self.state[index] is "0" else "0"

    def solved(self):
        return all(card is "." for card in self.state)

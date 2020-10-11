class Encrypter:
    def __init__(self, grid):
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)

        self._encrypted_message = ""
        self._current_x = None
        self._current_y = None
        self._visited_cells = []

    def encrypt(self, direction):
        self._encrypted_message = ""
        self._current_x = None
        self._current_y = None
        self._visited_cells = []

        self.walk_to(self.width - 1, 0)

        if direction is "clockwise":
            self.encrypt_clockwise()
        else:
            self.encrypt_counter_clockwise()

        return self._encrypted_message

    def encrypt_clockwise(self):
        while not self.solved():
            self.walk_down()
            self.walk_left()
            self.walk_up()
            self.walk_right()

    def encrypt_counter_clockwise(self):
        while not self.solved():
            self.walk_left()
            self.walk_down()
            self.walk_right()
            self.walk_up()

    def solved(self):
        return len(self._encrypted_message) is self.width * self.height

    def walk_up(self):
        while self.can_walk_to(self._current_x, self._current_y - 1):
            self.walk_to(self._current_x, self._current_y - 1)

    def walk_down(self):
        while self.can_walk_to(self._current_x, self._current_y + 1):
            self.walk_to(self._current_x, self._current_y + 1)

    def walk_left(self):
        while self.can_walk_to(self._current_x - 1, self._current_y):
            self.walk_to(self._current_x - 1, self._current_y)

    def walk_right(self):
        while self.can_walk_to(self._current_x + 1, self._current_y):
            self.walk_to(self._current_x + 1, self._current_y)

    def can_walk_to(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and (x, y) not in self._visited_cells

    def walk_to(self, x, y):
        self._encrypted_message += self.grid[y][x]
        self._visited_cells.append((x, y))
        self._current_x = x
        self._current_y = y

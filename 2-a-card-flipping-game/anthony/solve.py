from game import Game


def solve(initial_state):
    game = Game(initial_state)

    if game.get_number_of_ones() % 2 is not 1:
        print("no solution")
        return

    solution = []
    while not game.solved():
        first_one = game.get_first_one()
        game.take(first_one)
        solution.append(str(first_one))

    print(" ".join(solution))

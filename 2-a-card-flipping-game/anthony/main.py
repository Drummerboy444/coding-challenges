from game import Game


# game = Game("101")
# print(game.successful())
# print(game.stuck())
# game.print()
# game.take(0)
# game.print()
# game.take(1)
# game.print()
# print(game.successful())
# print(game.stuck())


game = Game("100")
game.print()
game.take(0)
game.take(1)
game.take(2)
game.print()
print(game.stuck())
print(game.successful())




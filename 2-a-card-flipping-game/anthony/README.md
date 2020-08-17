# Proposition

Let `C1, C1, ..., CN` be the cards in a game of size `N`, where for all `i < N`, `Ci` is in `{ 0, 1 }`.

Then for all `N > 0`, the game is solvable if and only if `|{ Ci | Ci = 1 }|` is odd.

# Proof

Proven by induction.

## Base Case

If `N = 1`, then the proposition is trivially true.

## Inductive Step

Suppose that the proposition is true for `N`. Now consider the case `N + 1`.

First, if there are no `1`'s, then the game is not solvable and the number of `1`'s is even. So the proposition holds true.

Now assume that there is at least one `1` and that `N + 1` is odd. Then our first move will be to take this `1`. We are now left with 2 disconnected sub-games. The one on the left looks like: `0, 0, ..., 0, 1`. Which is trivially solvable. The one on the right now has an odd number of `1`'s, as we removed one `1` from the game, and flipped the adjacent card. This sub-game is also solvable by induction so the initial game is solvable.

Finally, assume that there is at least one `1` and that `N + 1` is even. Suppose that card `Ci` is a `1` and that we take it. Before we flip adjacent cards, there is certainly an odd number of `1`'s in one of the disconnected sub-games and an even number of `1`'s in the other. After we flip the adjacent cards, the sub-game with an odd number of `1`'s will now have an even number of `1`'s (it will also certainly have at least one card, as it initially had an odd number of cards and so must have at least one card). This sub-game is not solvable by induction and so the game itself is not solvable for `i` and, since `i` was an arbitrary choice, the game is not solvable for any `i`.

We've shown that if the number of `1`'s is odd then the game is solvable, and that if the number of `1`'s is not odd (i.e. even) then the game is not solvable. So the proposition is true for `N + 1` and so is proven by induction. 

from typing import Dict, List


class FlipGame:
    __flip: Dict[str, str] = {"0": "1", "1": "0", ".": "."}

    def __init__(self, cards: str) -> None:
        self.cards = cards
        self.solution = self.__solve_flip()

    def __solve_flip(self) -> str:
        if self.__unsolvable():
            return "No Solution"

        move_list: List[int] = []
        cards_list: List[str] = [i for i in self.cards]

        while "1" in cards_list:
            first_one = cards_list.index("1")

            cards_list[first_one] = "."
            move_list.append(first_one)

            self.__flip_neighbour(cards_list, first_one - 1)
            self.__flip_neighbour(cards_list, first_one + 1)

        return " ".join(map(str, move_list))

    def __unsolvable(self) -> bool:
        return not self.cards.count("1") % 2

    def __flip_neighbour(self, cards_list: List[str], index: int) -> None:
        if -1 < index < len(cards_list):
            cards_list[index] = self.__flip[cards_list[index]]


if __name__ == "__main__":
    print(FlipGame("0100110").solution)
    print(FlipGame("001011011101001001000").solution)
    print(FlipGame("1010010101001011011001011101111").solution)
    print(FlipGame("1101110110000001010111011100110").solution)
    print(
        FlipGame(
            "010111111111100100101000100110111000101111001001011011000011000"
        ).solution
    )

def main():
    solveGame('0100110')
    solveGame('01001100111')
    solveGame('100001100101000')

    solveGame('001011011101001001000')
    solveGame('1010010101001011011001011101111')
    solveGame('1101110110000001010111011100110')

    # solveGame('010111111111100100101000100110111000101111001001011011000011000')   
    
def solveGame(input):
    gameState = readInputIntoList(input)
    firstInPlayCardIndex = 0
    solution = []

    for cardIndex in range(len(gameState)):
        if isFaceUp(gameState[cardIndex]):
            removeCardsInRangeDescending(solution, cardIndex, firstInPlayCardIndex)
            flipCard(gameState, cardIndex + 1)
            firstInPlayCardIndex = cardIndex + 1        

    if firstInPlayCardIndex < len(gameState):
        print("no solution")
    else:
        print(" ".join(solution))

def isFaceUp(card):
    return card is "1"

def removeCardsInRangeDescending(solution, start, end):
    for card in range(start, end - 1, -1):
        solution.append(str(card))

def flipCard(gameState, cardIndex):
    if cardIndex < len(gameState):
        gameState[cardIndex] = "1" if gameState[cardIndex] is "0" else "0"

def readInputIntoList(input):
    if not isinstance(input, str):
        raise Exception("Please provide a valid string input")
    inputList = list(input)
    if not all(element in ('0', '1') for element in inputList):
        raise Exception("Please ensure input string only consists of 1s and 0s")
    return inputList


if __name__ == "__main__":
        main()
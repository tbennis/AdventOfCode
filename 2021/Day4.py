def crossNumber(card, number):
    for i in range(len(card)):
        for cell in card[i].split(' '):
            if number == cell:
                newRow = ['-1' if i == number else i for i in card[i].split(' ')]
                card[i] = ' '.join(newRow)
    return card

def checkBingo(card):
    # check rows
    for row in card:
        if row == '-1 -1 -1 -1 -1':
            return True
    # check columns
    card = [row.split(' ') for row in card]
    for i in range(4):
        if int(card[0][i]) + int(card[1][i]) + int(card[2][i]) + int(card[3][i]) + int(card[4][i]) == -5:
            return True
    # no bingo
    return False

def calcSolution(card, number):
    solution = 0
    for row in card:
        for cell in row.split(' '):
            if cell != '-1':
                solution += int(cell)
    solution *= int(number)
    return solution

with open('Input4.txt') as f:
    input = f.read()

bingoNumbers = input.splitlines()[0].split(',')
bingoCards = input.splitlines()[2:]
cardList = []
currentCard = []
for i in range(1, len(bingoCards)+1):
    if i%6 == 5:
        currentCard += [' '.join(bingoCards[i-1].split())]
        cardList += [currentCard]
        currentCard = []
    elif i%6 != 0:
        currentCard += [' '.join(bingoCards[i-1].split())]

abort = False
firstWin = ''
firstWinNumber = ''
for i in bingoNumbers:
    removeList = []
    for j in range(len(cardList)):
        crossedCard = crossNumber(cardList[j], i)
        cardList[j] = crossedCard
        if checkBingo(crossedCard):
            if firstWin == '':
                firstWin = crossedCard
                firstWinNumber = int(i)
            if len(cardList) == 1:
                lastWin = crossedCard
                lastWinNumber = int(i)
                abort = True
            else:
                removeList += [cardList[j]]
    for k in removeList:
        cardList.remove(k)
    if abort:
        break
print(calcSolution(firstWin, firstWinNumber))
print(calcSolution(lastWin, lastWinNumber))
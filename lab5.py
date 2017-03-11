import random

def roll_dice():
    numberCount = [0]*12
    rolls = 0
    while rolls < 10000:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        numberCount[total - 1] += 1
        rolls += 1
    print(numberCount)

def main():
    startCount = 0
    word = input('Enter a word: ')
    wordList = []
    while word != '':
        start = word[0]
        for i in word:
            if i == start:
                startCount += 1
        if startCount > 1:
            wordList += [word]
        word = input('Enter a word: ')
        startCount = 0
    print(wordList)

def ssort(someList):
    listLength = len(someList)
    counter = 0
    forCounter = 0
    newList = []

    while counter < listLength:
        minimum = min(someList)
        for i in someList:
            forCounter += 1
            if i == minimum:
                newList += [minimum]
                del(someList[forCounter - 1])
        forCounter = 0
        counter += 1
    print(newList)

def blackjack_total(cards):
    total = 0
    for i in cards:
        if i in '23456789':
            total += int(i)
        elif i in 'TJQK':
            total += 10
        elif i == 'A':
            total += 11
    if total > 21:
        for i in cards:
            if i == 'A':
                total -= 10
    return total

def casino_rules():
    deals = 0
    score17 = 0
    score18 = 0
    score19 = 0
    score20 = 0
    score21 = 0
    naturalBJ = 0
    bust = 0
    cardsDealt = 2
    deck = [2]*4 + [3]*4 + [4]*4 + [5]*4 + [6]*4 + [7]*4 + [8]*4 + \
     [9]*4 + ['T']*4 + ['J']*4 + ['Q']*4 + ['K']*4 + ['A']*4
    playingDeck = str(deck)
    random.shuffle(deck)
    while deals < 10000:
        while len(playingDeck) > 0:
            hand = ''
            hand = playingDeck[0] + playingDeck[1]
            handTotal = blackjack_total(hand)
            if handTotal < 17:
                hand += playingDeck[2]
            else:
                if handTotal == 17:
                    score17 += 1
                    break
                elif handTotal == 18:
                    score18 += 1
                    break
                elif handTotal == 19:
                    score19 += 1
                    break
                elif handTotal == 20:
                    score20 += 1
                    break
                elif handTotal == 21 and cardsDealt == 2:
                    naturalBJ += 1
                    break
                elif handTotal == 21 and cardsDealt > 2:
                    score21 += 1
                    break
                elif handTotal > 21:
                    bust += 1
            
        deals += 1
        cardsDealt = 2





#roll_dice()
#main()
#ssort([3,5,2,8,1,9])
#blackjack_total('KA3')
casino_rules()

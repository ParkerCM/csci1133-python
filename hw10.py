import random

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.vDict = {'Ace':'1','2':'2','3':'3','4':'4','5':'5','6':'6',\
        '7':'7','8':'8','9':'9','10':'10','Jack':'11','Queen':'12','King':'13'}
        self.pvDict = {'1':'Ace','2':'2','3':'3','4':'4','5':'5','6':'6',\
        '7':'7','8':'8','9':'9','10':'10','Jack':'Jack','Queen':'Queen','King':'King'}
        self.sDict = {'1':'Spades','2':'Clubs','3':'Hearts','4':'Diamonds'}

    def getValue(self):
        return self.vDict[self.value]

    def getSuit(self):
        return self.sDict[self.suit]

    def __str__(self):
        return str(self.pvDict[self.value]) + ' of ' + str(self.sDict[self.suit])

class Carddeck():
    def __init__(self, deckList):
        self.deck = deckList #Manipulated
        self.deck2 = self.deck[0:52] #Control
        self.currentIndex = 0

    def __repr__(self):
        x = []
        count = 0
        while count < 52:
            x.append(str(self.deck[count]))
            count += 1
        return str(x)

    def shuffle(self):
        random.shuffle(self.deck)

    def dealcards(self, num):
        dealt = []
        remove = []
        count = 0
        if num + self.currentIndex < len(self.deck):#More cards in deck than draw amount
            while count < num:
                dealt.append(self.deck[self.currentIndex])
                count += 1
                self.currentIndex += 1
        else:
            while self.currentIndex < len(self.deck):
                dealt.append(self.deck[self.currentIndex])
                remove.append(self.deck[self.currentIndex])
                self.currentIndex += 1

            del self.deck[:]
            for i in self.deck2:
                self.deck.append(i)
            self.shuffle()
            self.currentIndex = 0

            count = 0
            for i in remove:
                while count < len(self.deck):
                    if i == self.deck[count]:
                        del self.deck[count]
                    count += 1
                count = 0

            count = len(dealt)
            while count <= num:
                dealt.append(self.deck[self.currentIndex])
                count += 1
                self.currentIndex += 1

        return dealt

class Pokerhand():
    def __init__(self, cards):
        self.hand = cards

    def newHand(self, obj):
        self.hand = obj.dealcards(5)

    def __repr__(self):
        x = []
        for i in self.hand:
            x.append(str(i))
        return str(x)

    def rank(self):
        numOfSuitsDict = {'Spades':0,'Clubs':0,'Hearts':0,'Diamonds':0}
        numOfValuesDict = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,\
        '11':0,'12':0,'13':0}
        seq = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6',\
        '7':'7','8':'8','9':'9','10':'10','Jack':'11','Queen':'12','King':'13'}
        straight = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9],[6,7,8,9,10],\
        [7,8,9,10,11],[8,9,10,11,12],[9,10,11,12,13],[1,10,11,12,13]]
        cardRange = list(range(1,14))
        count = 0
        numOfSuits = 0
        numOfValues = 0
        match = False
        while count < 5:
            suit = self.hand[count].getSuit()
            value = self.hand[count].getValue()
            numOfSuitsDict[suit] += 1
            numOfValuesDict[value] += 1
            count += 1

        for i in numOfSuitsDict:
            if numOfSuitsDict[i] > 0:
                numOfSuits += 1
        for i in numOfValuesDict:
            if numOfValuesDict[i] > 0:
                numOfValues += 1

        valList = []
        for i in numOfValuesDict:
            valCounter = 0
            if numOfValuesDict[i] != 0:
                while valCounter < numOfValuesDict[i]:
                    valList.append(int(i))
                    valCounter += 1

        valList.sort()

        #Check full house
        if valList[0] == valList[1] and valList[2] == valList[3] and\
         valList[3] == valList[4] or valList[0] == valList[1] and\
          valList[1] == valList[2] and valList[3] == valList[4]:
            return 6

        #Check flush
        if numOfSuits == 1:
            #Check straight flush
            if numOfValues == 5:
                if valList in straight:
                    return 8
            return 5

        #Check straight
        elif valList in straight:
            return 4

        #Check 4 of a kind
        for i in cardRange:
            if valList.count(i) == 4:
                match = True
        if match is True:
            return 7

        #Check 3 of a kind
        for i in cardRange:
            if valList.count(i) == 3:
                match = True
        if match is True:
            return 3

        #Check two pair
        pairCount = 0
        for i in cardRange:
            if valList.count(i) == 2:
                pairCount += 1
        if pairCount == 2:
            return 2

        #Check pair
        for i in cardRange:
            if valList.count(i) == 2:
                match = True
        if match is True:
            return 1

        #High card
        else:
            return 0



def main():
    obj1 = Card('Ace', '1')
    obj2 = Card('2', '1')
    obj3 = Card('3', '1')
    obj4 = Card('4', '1')
    obj5 = Card('5', '1')
    obj6 = Card('6', '1')
    obj7 = Card('7', '1')
    obj8 = Card('8', '1')
    obj9 = Card('9', '1')
    obj10 = Card('10', '1')
    obj11 = Card('Jack', '1')
    obj12 = Card('Queen', '1')
    obj13 = Card('King', '1')
    obj14 = Card('Ace', '2')
    obj15 = Card('2', '2')
    obj16 = Card('3', '2')
    obj17 = Card('4', '2')
    obj18 = Card('5', '2')
    obj19 = Card('6', '2')
    obj20 = Card('7', '2')
    obj21 = Card('8', '2')
    obj22 = Card('9', '2')
    obj23 = Card('10', '2')
    obj24 = Card('Jack', '2')
    obj25 = Card('Queen', '2')
    obj26 = Card('King', '2')
    obj27 = Card('Ace', '3')
    obj28 = Card('2', '3')
    obj29 = Card('3', '3')
    obj30 = Card('4', '3')
    obj31 = Card('5', '3')
    obj32 = Card('6', '3')
    obj33 = Card('7', '3')
    obj34 = Card('8', '3')
    obj35 = Card('9', '3')
    obj36 = Card('10', '3')
    obj37 = Card('Jack', '3')
    obj38 = Card('Queen', '3')
    obj39 = Card('King', '3')
    obj40 = Card('Ace', '4')
    obj41 = Card('2', '4')
    obj42 = Card('3', '4')
    obj43 = Card('4', '4')
    obj44 = Card('5', '4')
    obj45 = Card('6', '4')
    obj46 = Card('7', '4')
    obj47 = Card('8', '4')
    obj48 = Card('9', '4')
    obj49 = Card('10', '4')
    obj50 = Card('Jack', '4')
    obj51 = Card('Queen', '4')
    obj52 = Card('King', '4')

    deck = [obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9, obj10, obj11,\
    obj12, obj13, obj14, obj15, obj16, obj17, obj18, obj19, obj20, obj21, obj22,\
    obj23, obj24, obj25, obj26, obj27, obj28, obj29, obj30, obj31, obj32, obj33,\
    obj34, obj35, obj36, obj37, obj38, obj39, obj40, obj41, obj42, obj43, obj44,\
    obj45, obj46, obj47, obj48, obj49, obj50, obj51, obj52]

    freq = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    handKey = {0:'High Card',1:'One pair',2:'Two pair',3:'Three of a kind',4:'Straight',\
    5:'Flush',6:'Full house',7:'Four of a kind',8:'Straight flush'}
    count = 0

    print('\n\nSimulating...\n\n')


    cdObj = Carddeck(deck)
    cdObj.shuffle()
    hand = cdObj.dealcards(5)
    phObj = Pokerhand(hand)

    while count < 100000:
        value = phObj.rank()
        phObj.newHand(cdObj)
        freq[value] += 1
        count += 1

    count = 0
    keys = list(freq.keys())
    values = list(freq.values())
    freqList = []

    while count < len(keys):
        freqList.append([values[count], keys[count]])
        count += 1

    freqList.sort()
    count = 0

    while count < len(freqList):
        print(str(handKey[freqList[count][1]])+': '+str(freqList[count][0]))
        count += 1
main()

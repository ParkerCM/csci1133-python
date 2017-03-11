import math

def shortestDist(initialList):
    distances = []
    listLen = len(initialList) - 1
    currentPair = 0
    otherPair = 0

    while currentPair <= listLen:
        while otherPair <= listLen:
            if otherPair == currentPair:
                otherPair += 1
            else:
                x1 = initialList[currentPair][0]
                y1 = initialList[currentPair][1]
                x2 = initialList[otherPair][0]
                y2 = initialList[otherPair][1]
                dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                distances.append(dist)
                otherPair += 1
        currentPair += 1
        otherPair = 0

    smallest = distances[0]
    for i in distances:
        if i < smallest:
            smallest = i

    return smallest

def unitTest():
    hoyehh = shortestDist([[45, -99], [24, 83], [-48, -68], [-97, 99], \
    [-8, -77], [-2, 50], [44, 41], [-48, -58], \
    [-1, 53], [14, 86], [31, 94], [12, -91], \
    [33, 50], [82, 72], [83, -90], [10, 78], \
    [7, -22], [90, -88], [-21, 5], [6, 23]])
    print(hoyehh)

def gameState(game):
    isDraw = True
    row = 0
    col = 0
    a = ''
    b = ''
    c = ''

    for i in game:
        for j in i:
            if j == '':
                isDraw = False

    # Horizontal Wins
    while row <= 2:
        while col <= 2:
            if col == 0:
                a = game[row][col]
                col += 1
            elif col == 1:
                b = game[row][col]
                col += 1
            elif col == 2:
                c = game[row][col]
                col += 1
        row += 1
        col = 0
        if a == b and b == c:
            if a in 'XO':
                return a

    # Vertical Wins
    row = 0
    col = 0
    while col <= 2:
        while row <= 2:
            if row == 0:
                a = game[row][col]
                row += 1
            elif row == 1:
                b = game[row][col]
                row += 1
            elif row == 2:
                c = game[row][col]
                row += 1
        col += 1
        row = 0
        if a == b and b == c:
            if a in 'XO':
                return a

    # Diagonal Wins
    row = 0
    col = 0
    while row <= 2:
        if row == 0:
            a = game[row][col]
            row += 1
            col += 1
        elif row == 1:
            b = game[row][col]
            row += 1
            col += 1
        elif row == 2:
            c = game[row][col]
            row += 1
            col += 1
    if a == b and b == c:
        if a in 'XO':
            return a

    row = 0
    col = 2
    while row <= 2:
        if row == 0:
            a = game[row][col]
            row += 1
            col -= 1
        elif row == 1:
            b = game[row][col]
            row += 1
            col-= 1
        elif row == 2:
            c = game[row][col]
            row += 1
            col -= 1
    if a == b and b == c:
        if a in 'XO':
            return a

    if isDraw:
        return 'D'
    else:
        return ''

def testTTT():
    results = []
    xwins = [['X', '', 'O'], ['X', 'O', ''], ['X', '', 'O']]
    owins = [['O', '', 'X'], ['X', 'O', ''], ['X', '', 'O']]
    draw = [['O', 'X', 'O'], ['X', 'X', 'O'], ['X', 'O', 'X']]
    nothing = [['', 'X', 'O'], ['X', 'O', ''], ['X', '', 'O']]

    x = gameState(xwins)
    o = gameState(owins)
    d = gameState(draw)
    n = gameState(nothing)
    results += x, o, d, n

    for i in results:
        if i is 'X':
            print('X wins')
        elif i is 'O':
            print('O wins')
        elif i is 'D':
            print('Draw')
        elif i is '':
            print('No Win, No Draw')

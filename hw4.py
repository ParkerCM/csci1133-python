def romanTotal(roman):
    if roman == 'M':
        return(1000)
    elif roman == 'D':
        return(500)
    elif roman == 'C':
        return(100)
    elif roman == 'L':
        return(50)
    elif roman == 'X':
        return(10)
    elif roman == 'V':
        return(5)
    elif roman == 'I':
        return(1)

def validSubtraction(x, y):
    if (x == 50 or x == 100 or x == 500 or x == 1000) and (y == 1):
        return False
    elif (x == 1 or x == 5 or x == 500 or x == 1000) and (y == 10):
        return False
    elif (x == 1 or x == 5 or x == 10 or x == 50) and (y == 100):
        return False
    elif ( y == 5 or y == 50 or y == 500):
        return False
    else:
        return True

def romanNumbers(roman):
    total = 0
    aheadCount = 1
    behindCount = 0
    romLen = len(roman)
    for i in roman:
        if i not in 'IVXLCDM':
            return(0)
    if romLen == 1:
        total += romanTotal(roman[0])
    else:
        if romLen - 1 >= 3:
            index0 = 0
            index1 = 1
            index2 = 2
            index3 = 3
            while index3 <= romLen - 1:
                #Checks if a letter is repeated four times in a row
                if romanTotal(roman[index0]) == romanTotal(roman[index1]) \
                and romanTotal(roman[index1]) == romanTotal(roman[index2]) \
                and romanTotal(roman[index2]) == romanTotal(roman[index3]):
                    return 0
                index0 += 1
                index1 += 1
                index2 += 1
                index3 += 1
        while aheadCount <= romLen - 1:
            x = romanTotal(roman[aheadCount])
            y = romanTotal(roman[behindCount])
            if x - y > 0:
                canSub = validSubtraction(x, y) # Makes sure subtraction obeys the laws of roman numerals
                if canSub:
                    total += (x - y)
                    aheadCount += 2
                    behindCount += 2
                else:
                    return 0 # Invalid roman numeral
            elif x - y < 0 and aheadCount == romLen - 1:
                total += (x + y)
                aheadCount += 1
                behindCount += 1
            elif x - y < 0:
                total += y
                aheadCount += 1
                behindCount += 1
            elif x - y == 0 and aheadCount == romLen - 1:
                total += (x + y)
                aheadCount += 1
                behindCount += 1
            elif x - y == 0:
                total += y
                aheadCount += 1
                behindCount += 1
    return(total)

def rlEncode(somelist):
    encodedList = []
    count = 1
    lastChar = None
    for i in somelist:
        if i != lastChar:
            if lastChar:
                encodedList += [lastChar]
                encodedList += [count]
            count = 1
            lastChar = i
        else:
            count += 1
    else:
        encodedList += [lastChar]
        encodedList += [count]

    return(encodedList)

def rlDecode(encodedList):
    count = 0
    decodedList = []
    for i in encodedList:
        if (count % 2 == 0) or count == 0:
            num = i
            count += 1
        else:
            decodedList += [num] * encodedList[count]
            count += 1
    return(decodedList)

def encodeTest():
    print(rlEncode([1,2,3,5,5,5,5,5,5,6,8,8,1,1,1,5,5,12,13,14,14]))

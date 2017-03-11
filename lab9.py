def makeDictionary(list1, list2):
    scoreDict =  {}
    length = len(list1)
    count = 0

    while count < length:
        scoreDict[list1[count]] = list2[count]
        count += 1
    return scoreDict

def getScore(name, dictionary):
    if name in dictionary:
        return dictionary[name]
    else:
        print("Error, not in dictionary.")
        return -1

def addDB(dictionary, str1, str2):
    if str1 in dictionary:
        dictionary[str1] += [str2]
    elif str1 not in dictionary:
        dictionary[str1] = str2

    if str2 in dictionary:
        dictionary[str2] += str1
    elif str2 not in dictionary:
        dictionary[str2] = str1

    print(dictionary)
cool = {'joe':'10', 'tom':'23', 'barb':'13', 'sue':'18', 'sally':'12'}
names = ['joe', 'tom', 'barb', 'sue', 'sally']
scores = [10,23,13,18,12]
addDB(cool, 'fred', '82')
addDB(cool, 'joe', '28')
addDB(cool, 'fred', '49')

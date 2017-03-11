def reverseAssoc(phonebook):
    name = []
    newDict = {}
    count = 0
    length = len(phonebook)
    value = list(phonebook.values())

    for i in phonebook:
        name.append(i)

    while count < length:
        newDict[value[count]] = name[count]
        count += 1

    return newDict

def getNumber():
    numDict = {'A':'2','B':'2','C':'2','D':'3','E':'3','F':'3',\
    'G':'4','H':'4','I':'4','J':'5','K':'5','L':'5','M':'6','N':'6',\
    'O':'6','P':'7','Q':'7','R':'7','S':'7','T':'8','U':'8','V':'8',\
    'W':'9','X':'9','Y':'9','Z':'9'}
    bank = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tempString = ''
    finalString = ''

    num = str(input("Enter a telephone number: "))

    while num != '':
        num = num.upper()
        for i in num:
            if i in bank: # Removes punctuation
                tempString += i
        for i in tempString:
            if i not in alpha: # Number, doesn't get converted
                finalString += i
            elif i in alpha: # Alpha, must be converted to number
                finalString += numDict[i]
        if len(finalString) == 10:
            finalString = finalString[:3] + '-' + finalString[3:6] + '-' + finalString[6:]
            print("Numeric telephone number is:", finalString)
        elif len(finalString) == 7:
            finalString = finalString[:3] + '-' + finalString[3:]
            print("Numeric telephone number is:", finalString)
        else:
            print("Invalid number!")
        finalString = ''
        tempString = ''

        num = str(input("Enter a telephone number: "))

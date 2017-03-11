def count(char, text):
    if len(text) == 0:
        return 0
    elif char == text[0]:
        return 1 + count(char, text[1:])
    else:
        return 0 + count(char, text[1:])

def isEqual(list1, list2):
    if len(list1) == 0 and len(list2) == 0:
        return True
    elif len(list1) != len(list2):
        return False
    elif list1[0] == list2[0]:
        return isEqual(list1[1:], list2[1:])
    else:
        return False

def convertBase(n, base):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 16:
        return 0
    elif n // base == 0:
        return str(n)
    else:
        rem = n % base
        n = n // base
        if rem >= 10:
            rem = alpha[rem - 10]
            return convertBase(n, base) + str(rem)
        return convertBase(n, base) + str(rem)

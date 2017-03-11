import os

def fileExists(name): #Determines if a file exists in directory
    x = os.path.isfile(name)
    if x:
        return True
    else:
        return False

def readFile(inFile, symbol): #Reads file for provided airport code and
    iFile = open(inFile, 'r') #appends line to a list
    flights = []

    line = iFile.readline()
    while line != '':
        if symbol in line:
            line = line.strip()
            flights.append(line)
        line = iFile.readline()
    iFile.close()
    return flights

def writeFile(outFile, data): #Writes line list to a file
    oFile = open(outFile, 'w')

    for i in data:
        oFile.write(i)
        oFile.write('\n')
    oFile.close()

def main():
    validName = False
    attempts = 0

    inFileName = input('Enter the source file name: ')

    while not validName:
        validName = fileExists(inFileName)
        if validName is False:
            attempts += 1
            if attempts == 3:
                return 0
            inFileName = input('File not found. Reenter: ')

    outFileName = input('Enter the output file name: ')
    outExists = fileExists(outFileName)

    if outExists:
        overwrite = input('File exists... overwrite? (y/n): ')
        if overwrite == 'y' or overwrite == 'Y':
            airport = input('Enter airport symbol: ')
            airport = airport.upper()
            listings = readFile(inFileName, airport)
            writeFile(outFileName, listings)
        elif overwrite == 'n' or overwrite == 'N':
            return 0
    else: #File does not exist, continue
        airport = input('Enter airport symbol: ')
        airport = airport.upper()
        listings = readFile(inFileName, airport)
        writeFile(outFileName, listings)

    print('Finished.')

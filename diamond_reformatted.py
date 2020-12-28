def printSpaces(numSpaces):
    for i in range(numSpaces):
        print(" ", end="")


def createDiamond(numLines):
    numSpaces = numLines
    listOfPrintedSymbols = []
    
    for i in range(numLines):
        printSpaces(numSpaces)
        symbolsToPrint = i + (i + 1)
        listOfPrintedSymbols.append(symbolsToPrint)
        for j in range(symbolsToPrint):
            print("*", end="")
        printSpaces(numSpaces)
        print()
        numSpaces = numSpaces - 1

    numSpaces = 2
    listPosition = numLines - 2

    for i in range(numLines - 1):
        printSpaces(numSpaces)
        
        for j in range(listOfPrintedSymbols[listPosition]):
            print("*", end="")
        printSpaces(numSpaces)
        print()
        numSpaces = numSpaces + 1
        listPosition = listPosition - 1

def main():
    while 1:
        numLines = int(input("Please enter number of lines for the Diamond: "))
        createDiamond(numLines)


if __name__ == "__main__":
    main()

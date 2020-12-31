
def makeTopBottom(lineSize):
    topBottom = ""
    for i in range(lineSize):
        topBottom += "*"
    return topBottom

def makeSpacedLine(numSpaces):
    spacedLine = "*"
    for i in range(numSpaces):
        spacedLine += " "
    spacedLine += "*"
    return spacedLine

def main():
    while 1:
        boxSize = int(input("Please enter a Number"))
        topBottom = makeTopBottom(boxSize)
        numSpaces = boxSize-2
        spacedLine = makeSpacedLine(numSpaces)
        print(topBottom)
        for i in range(numSpaces):
            print(spacedLine)
        print(topBottom)
    

if __name__== "__main__":
    main()

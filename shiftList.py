def getInput(numList):
    maxListLength = 5
    while len(numList) < maxListLength:
        number = input("Please enter a Number: ")
        numList.append(number)
    return numList

def makeChoice(numList):
    stopCheck = 0
    while(1):
        choice = input("Please enter 1 to Shift Left, 2 to Shift Right or 0 to exit the program")
        if choice == "1":
            shiftLeft(numList)
        elif choice == "2":
            shiftRight(numList)
        elif choice == "0":
            break
        else:
            print("Error on Input, Please Try Again")
    
def shiftLeft(numList):
    numList.insert(5,numList[0])
    numList.pop(0)
    print("List has Been shifted right:\n",numList)

def shiftRight(numList):
    numList.insert(0,numList[4])
    numList.pop(5)
    print("List has Been shifted right:\n",numList)



def main():
    numList = []
    numlist = getInput(numList)
    makeChoice(numList)
    



if __name__ == "__main__":
    main()

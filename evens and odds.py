def evens(x):
    for i in range(x):
        tmp = i % 2
        if tmp == 0:
            print(i)
        else:
            pass


def odds(x):
    for i in range(x):
        tmp = i % 2
        if tmp == 0:
            pass
        else:
            print(i)


while 1:
    choice = int(input("Please enter 0 for even or 1 for odd: "))

    if choice == 0:
        check = 0
        while check == 0:
            try:
                x = int(input("Please enter a number to get all even numbers up to the inputed number: "))
                evens(x)
                check = 1
            except ValueError:
                print("Error Input was not an Integer")
    elif choice == 1:
        check = 0
        while check == 0:
            try:
                x = int(input("Please enter a number to get all odd numbers up to the inputed number: "))
                odds(x)
                check = 1
            except ValueError:
                print("Error Input was not an Integer")

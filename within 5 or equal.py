while 1:
    x = int(input("Please enter a number"))
    y = int(input("Please enter a second number"))

    if x == y:
        print("Numbers are equal")

    elif x - y > 5 or y - x > 5 or x -y < -5 or y - x < -5:
        print("Numbers are not within 5 of each other")

    else:
        print("Numbers are within 5 of each other")


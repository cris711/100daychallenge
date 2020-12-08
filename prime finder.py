def prime(inp):
    for i in range(2, inp+1):
        for j in range(2, i+1):
            if (i == j):
                print(i, "is a prime number")
                break
            elif (i % j) == 0:
                break


def main():
    inp = int(input("Please enter an integer"))

    prime(inp)


if __name__ == "__main__":
    main()

def print_Spaces(spaces):
    for i in range(spaces):
        print(" ", end="")


def top_Down(inp):
    spaces = inp
    for i in range(inp):
        print_Spaces(spaces)
        tmp = i + (i + 1)
        for j in range(tmp):
            print("*", end="")
        print_Spaces(spaces)
        print()
        spaces = spaces - 1


def down_Top(inp):
    tmp = inp - 1
    spaces = 2
    for i in range(inp - 1):
        print_Spaces(spaces)
        tmp_run = ((tmp + tmp) - 1)
        for j in range(tmp_run):
            print("*", end="")
        print_Spaces(spaces)
        print()
        tmp = tmp - 1
        spaces = spaces + 1


def diamond(inp):
    top_Down(inp)
    down_Top(inp)


def main():
    inp = int(input("Please enter number: "))
    diamond(inp)


if __name__ == "__main__":
    main()

def cube(inp):
    for i in range(inp):
        cubic = (inp-i)**3
        print("Cube of ",(inp-i)," is: ", cubic)

def main():
    while 1:
        inp = int(input("Please enter a Number"))
        cube(inp)

if __name__ == "__main__":
    main()

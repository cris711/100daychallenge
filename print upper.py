class py_class():
    def __init__(self):
        self.inp = ""
    def get_String(self):
        self.inp = input("Please enter a string")

    def print_String(self):
        print(self.inp.upper())


def main():
    inp1 = py_class()
    inp1.get_String()
    inp1.print_String()


if __name__ == "__main__":
    main()

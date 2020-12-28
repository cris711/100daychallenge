def zero_counter(inp):
    parsed = inp.split("*")
    map_obj = map(int, parsed)
    int_list = list(map_obj)
    result = int_list[0] * int_list[1]
    result_str = str(result)
    print(result_str)
    num_zeros = 0

    for i in range(len(result_str)):
        if result_str[i] == "0":
            num_zeros += 1
        else:
            pass

    return num_zeros


def main():
    while 1:
        inp = input("Please enter a factorial number ex:20*60")
        num_zeros = zero_counter(inp)
        print("Number of zeros:", num_zeros)


if __name__ == "__main__":
    main()

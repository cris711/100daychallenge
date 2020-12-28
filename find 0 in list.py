def list_to_int(inp,inp_list):

    tmp_list = list(inp)
    neg_bool = 0
    length = len(tmp_list)
    for i in range(length):
        print("Index ", i, "contains :", tmp_list[i])
        if tmp_list[i].isspace():
            pass


        elif neg_bool == 1 and tmp_list[i] != "-":
            tmp = "-" + tmp_list[i]
            inp_list.append(float(tmp))
            neg_bool = 0

        elif tmp_list[i] == "-":
            neg_bool = 1


        else:
            inp_list.append(float(tmp_list[i]))



def zero_finder(inp_list):
    zero_check = 0
    for i in range(len(inp_list) - 2):
        test_num = (inp_list[i]) + (inp_list[i + 1]) + (inp_list[i + 2])
        print(test_num)
        if (test_num == 0):
            zero_check = 1
            print("Zero found at position [", i, "] ", inp_list[i], "+", inp_list[i + 1], "+", inp_list[i + 2], "=0")
        elif (i == (len(inp_list) - 3) and zero_check == 0):
            print("No three numbers in a row amount to zero")


def printer(inp_list):
    for i in range(len(inp_list)):
        print("list", i,":",inp_list[i])

def main():
    inp = input("Please enter a squence of numbers")

    inp_list = []
    list_to_int(inp,inp_list)
    printer(inp_list)
    zero_finder(inp_list)


if __name__ == "__main__":
    main()

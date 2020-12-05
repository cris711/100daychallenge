inp = input("Please enter file name to output to")
inp = inp + ".txt"
f = open(inp, "a")
buff = str(input("Please enter data: "))
f.write(buff)
f.close

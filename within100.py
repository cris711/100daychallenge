def compare(num):
    y = 1000 - num
    z = 2000 - num
    if y <= 100 and y >= -100:
        print("Number is within 100 of 1000")
        return
    elif z<=100 and z>=-100:
        print("Number is within 100 of 2000")
        return
    else:
        print("Number is not within 100 of 1000 nor 2000")
        return

while 1:
    x = float(input("Please Enter a Number:\n"))
    compare(x)


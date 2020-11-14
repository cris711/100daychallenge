
#main input area
while 1:
    #Getting user input
    x = int(input("Please Input a Number:\n"))
    y = int(input("Please Input a Second Number:\n"))
    #Boolean used in loop to assure operation entered is a valid input option
    check = False
    while check == False:
    
        inp = input("Please Input an operation (+-*/) ")

        if inp=='+':
            ans = x + y
            print(x,"+",y,"=",ans)
            check = True
        elif inp=='-':
            ans = x - y
            print(x,"-",y,"=",ans)
            check = True
        elif inp =='*':
            ans = x * y
            print(x,"*",y,"=",ans)
            check = True
        elif inp =='/':
            ans = x / y
            print(x,"/",y,"=",ans)
            check = True

        else:
            print("Error Incorrect operation entered")


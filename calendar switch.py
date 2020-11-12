#Defining the functions to be called from switcher
def one():
    return "January"
 
def two():
    return "February"
 
def three():
    return "March"
 
def four():
    return "April"
 
def five():
    return "May"
 
def six():
    return "June"
 
def seven():
    return "July"
 
def eight():
    return "August"
 
def nine():
    return "September"
 
def ten():
    return "October"
 
def eleven():
    return "November"
 
def twelve():
    return "December"
 
#Creating dictionary to call the functions from
switcher = {
            '1': one(),
            '2': two(),
            '3': three(),
            '4': four(),
            '5': five(),
            '6': six(),
            '7': seven(),
            '8': eight(),
            '9': nine(),
            '10': ten(),
            '11': eleven(),
            '12': twelve(),
}
#main input area
while 1:
    #Getting user input
    inp = input("Please Input a Number Corresponding to a Month of the Year: \n(Ex:1=January)\n")
    #Calling the switcher dictionary of functions
    print("result:",switcher.get(inp,"Error Incorrect Input"))



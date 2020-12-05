p = float(input("Please enter Principal amount"))
r = float(input("Please enter rate of interest in decimal form(ex:3% == .03)"))
t = float(input("Please enter number of years"))

a = p*(1+(r*t))

print("Initial Amount: ",p," with interest rate: ",r," over the span of: ",t," years results in:", a)

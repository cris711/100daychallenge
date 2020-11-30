inp = input("Please enter a string")
result = ""
orig = ""
s = 4
x = 8
pos = len(inp) - 1
for i in range(len(inp)):
    char = inp[pos]  #starting at end to reverse input
    result += chr((ord(char) + s-97) % 26 + 97) #Shifting the (backwords)og value
    result += chr((ord(char) + x - 97) % 26 + 97) #first salt
    result += chr((ord(char) + 1 - 97) % 26 + 97)   #second salt
    pos -= 1
print(result)

for i in range(0, len(result), 3):
    char = result[i]
    orig += chr((ord(char) - s-97) % 26 + 97)
    i += 1
    i += 1

orig = orig[::-1]
print(orig)

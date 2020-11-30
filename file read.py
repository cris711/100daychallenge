file=open("text.txt","r")
print("Name of File: ", file.name, "\n")
data = file.read()
occur = data.count("4")
print("Number of 4's in Document: ", occur,"\n")
print(data)


file.close()

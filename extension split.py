import os.path
filename = input("Please enter a File name with its extension EX:file.txt\n")
ext = os.path.splitext(filename)[1]
print("File Extension:",ext)


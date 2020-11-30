x = int(input("Please enter number of rows: "))
lst = [0]* x
for i in range(x):
    print("Please Enter row", i+1, "quantity")
    tmp=int(input())
    lst[i] = tmp
else:
    print("Input Successful")

for i in range(x):
    print(i,"| ", '+'*lst[i])



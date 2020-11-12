print("Welcome human, you have ventured far from your home into a dangerous world")
print("You must escape from this place, quickly now leave while you can")
check = False
while check == False:
    choice = input("Options: 1:North - peer:Perceive area\n")
    if choice == '1':
        check = True
    elif choice == 'peer':
        print("you are standing in what appears to be a dark hallway")
        print("you are surrounded by walls on all sides minus the direction in front of you")
    else:
        print("check your input, quicknly now you must hurry!")

check = False
print("you are standing in a path that splits into 3 sections (north, east and west)")

while check == False:
    choice = input("Options: 1:North - 2:East - 3:South - 4:West - peer:Perceive area\n")
    if choice == '1':
        check = True
    elif choice == '2':
        check = True
    elif choice == '3':
        check = True
    elif choice == '4':
        check = True
    elif choice == 'peer':
        print("you are standing in what appears to be a dark hallway")
        print("you are surrounded by pathways on all sides")
    else:
        print("check your input, quicknly now you must hurry!")


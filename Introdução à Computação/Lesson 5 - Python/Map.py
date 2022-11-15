map = (["A","B","C"],["D","E","F"],["G","H","I"])

start = map[1][1]

x,y = 1,1

player = x, y

command = ""

print(" ___ ___ ___\n|_A_|_B_|_C_|\n|_D_|_E_|_F_|\n|_G_|_H_|_I_|")
print("\nPlayer is in Room " + map[y][x])

while command != "exit":
    # Run game command
    command = input("\nWhere do you want to go?\n")

    if command == "north":
        # North movement
        if y - 1 >= 0:
            y = y - 1
            print("\nYou are now in room " + map[y][x])
        else:
            print ("\nYou can't go further than that!")

    elif command == "south":
        # South movement
        if y + 1 <= 2:
            y = y + 1
            print("\nYou are now in room " + map[y][x])
        else:
            print ("\nYou can't go further than that!")

    elif command == "east":
        # East movement
        if x + 1 <= 2:
            x = x + 1
            print("\nYou are now in room " + map[y][x])
        else:
            print ("\nYou can't go further than that!")

    elif command == "west":
        #West movement
        if x - 1 >= 0:
            x = x - 1
            print("\nYou are now in room " + map[y][x])
        else:
            print ("\nYou can't go further than that!")
    elif command == "exit":
        print("")
    else:
        print("Movement not available")



#G C I [0][2],[2][2]



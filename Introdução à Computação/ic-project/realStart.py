
###########
#Variables#
###########
map = (["A","B","C"],["D","E","F"],["G","H","I"]) #Map from each room
command = "" #Empty variable for the future inputs
x,y = 0,0 #Initial position

######################
#Introductive message#
######################
def introduction(): #Function for having a little introduction and for the player set his name
    print ("\033[1;36mWelcome to the Dragon Adventure! In this game you will control a group of friends through the game.\n") #A little introduction message
    print("What's your name adventured?") #Print a question for the player's name

    name = input("\033[1;0m") #The player should enter his name
    greeting = "\n\033[1;36mGreat name! " + name + ", let's start our journey!\n" #A personalized welcome message

    print(greeting) #Print the welcome message
    print("So... where you wanna go first? \n\033[1;35m Castle\n Forest \n Village \n Church") #First path choose of the game
    init_path()

###############################################
#Function for the first location of the player#
###############################################
def init_path():
 command = input("\033[1;0m")
 if (command == "Castle"):
     print("\033[1;36m\nYou have moved to the Abandoned Castle!\n")
     castle()
 elif (command == "Forest"):
     print("\033[1;36m\nYou have moved to the Haunted Forest\n")
 elif (command == "Village"):
     print("\033[1;36m\nYou have moved to the Griffin Village!\n")
 elif (command == "Fortress"):
     print("\033[1;36m\nYou have moved to the Great Fortress!\n")
 elif (command == "Church"):
     print ("\033[1;36m\nYou have moved to the Old Church!\n")
 else:
     print ("\033[1;36m\nI don't know here is that location, " + command + "!\nChoose one location that I know, please!")
     init_path()


############
#Castle map#
############
def castle():
    global map
    global command
    global x,y

    x,y = 1,1 #Initial position

    print(" ___ ___ ___\n|_A_|_B_|_C_|\n|_D_|_E_|_F_|\n|_G_|_H_|_I_|") #Ilustrative map
    print("\nPlayer is in Room " + map[y][x] + ". Explore!") #First player location

    while command != "exit":
        # Run game command
        command = input("\nWhere do you want to go?\n")

        if command == "north": # North movement
            north()

        elif command == "south": # South movement
            south()

        elif command == "east": # East movement
            east()

        elif command == "west": #West movement
            west()

        else:
            print("Movement not available")

############
#Directions#
############
def north(): #Direction north
    global x,y
    if y - 1 >= 0: 
        y = y - 1
        print("\nYou are now in room " + map[y][x]) #Print current location after the move
    else:
        print ("\nYou can't go futher than that!") #Border of the room

def south(): #Direction south
    global x,y
    if y + 1 <= 2:
        y = y + 1
        print("\nYou are now in room " + map[y][x]) #Print current location after the move
    else:
        print ("\nYou can't go futher than that!") #Border of the room

def east(): #Direction east
    global x,y
    if x + 1 <= 2:
        x = x + 1
        print("\nYou are now in room " + map[y][x]) #Print current location after the move
    else:
        print ("\nYou can't go futher than that!") #Border of the room

def west():
    global x,y
    if x - 1 >= 0:
        x = x - 1
        print("\nYou are now in room " + map[y][x]) #Print current location after the move
    else:
        print ("\nYou can't go futher than that!") #Border of the room


introduction()
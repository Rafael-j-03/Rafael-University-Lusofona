from ctypes.wintypes import HPALETTE
import sys

def introduction(): #Function for having a little introduction and for the player set his name
 print ("\033[1;36mWelcome to the Dragon Adventure!\n") #A little introduction message
 print("What's your name adventured?") #Print a question for the player's name
 name = input("\033[1;0m") #The player should enter his name
 greeting = "\n\033[1;36mGreat name! " + name + ", let's start our journey!\n" #A personalized welcome message
 print(greeting) #Print the welcome message
 print("So... where you wanna go first? \n\033[1;35m Castle\n Forest \n Village \n Church") #First path choose of the game

def path(): #Function for the first location of the player
 command = input("\033[1;0m")
 if (command == "Castle"):
     print("\033[1;36m\nYou have moved to the Abandoned Castle!\n")
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
     path()


#Functions order
introduction()
path()

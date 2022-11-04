rooms = {

            'Hall' : { 
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'east'  : 'Living Room',
                  'item'  : 'knife'
                },
            'Dining Room' : {
                  'west'  : 'Hall',
                  'south' : 'Living Room',
                  'east'  : 'Garden',
                  'item'  : 'matchbox'
                },
            'Living Room' : {
                  'north' : 'Dining Room',
                  'west'  : 'Kitchen',
                  'item'  : 'monster'
                },
            'Garden' : {
                  'west'  : 'Dining Room'
            }

         }


def path(): #Function for the first location of the player
 command = input("\033[1;0m")
 if (command == "North"):
     print("\033[1;36m\nYou have moved to North!\n")
 elif (command == "South"):
     print("\033[1;36m\nYou have moved to South\n")
 elif (command == "East"):
     print("\033[1;36m\nYou have moved to East!\n")
 elif (command == "West"):
     print("\033[1;36m\nYou have moved to West\n")
 else:
     print ("\033[1;36m\nI don't know here is that location, " + command + "!\nChoose one location that I know, please!")
     path()

path()
    
def roomA():
  directions = ["east","south"]
  print("You are in Room A, where do you wanna go?")
  userInput = ""
  while userInput not in directions:
    print("Options: " + str(directions))
    userInput = input()
    if userInput == "east":
      roomB()
    elif userInput == "south":
      roomD()
    else: 
      print("You can't go that way!")

def roomB():
  directions = ["west","east","south"]
  print("You are in Room B, where do you wanna go?")
  userInput = ""
  while userInput not in directions:
    print("Options: " + str(directions))
    userInput = input()
    if userInput == "west":
      roomA()
    if userInput == "east":
      roomC()
    elif userInput == "south":
      roomE()
    else:
      print("You can't go that way!")

def roomC():
  directions = ["west","south"]
  print("You are in Room C, where do you wann go?")
  userInput = ""
  while userInput not in directions:
    print("Options: " + str(directions))
    userInput = input()
    if userInput == "west":
      roomB()
    elif userInput == "south":
      roomF()
    else:
      print("You can't go that way!")

def roomD():
  directions = ["north","east"]
  print("You are in room D, where do you wanna go?")
  userInput = ""
  while userInput not in directions:
    print("Options: " + str(directions))
    userInput = input()
    if userInput == "north":
      roomA()
    elif userInput == "east":
      roomE()
    else:
      print("You can't go that way!")

def roomE():
  directions = ["north","west","east"]
  print("You are in Room E, where do you wanna go?")
  userInput = ""
  while userInput not in directions:
    print("Options: " + str(directions))
    userInput = input()
    if userInput == "north":
      roomB()
    elif userInput == "west":
      roomD()
    elif userInput == "east":
      roomF()
    else: 
      print("You can't go that way!")

def roomF():
  directions = ["north","west"]
  print("You are in Room F, where do you wanna go?")
  userInput = ""
  while userInput not in directions:
    print("Options: " + str(directions))
    userInput = input()
    if userInput == "north":
      roomC()
    elif userInput == "west":
      roomE()
    else: 
      print("You can't go that way!")

roomA()
    
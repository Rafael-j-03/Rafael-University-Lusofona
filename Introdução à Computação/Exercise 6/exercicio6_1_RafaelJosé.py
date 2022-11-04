#Variables
txt = open("lorem.txt" , "r") #Read the file

lines = txt.readlines() #Lines from the txt


#Prints
print("\nLinha 3 " + lines[2]) #Print the thrid 

print("\n") #Print a empty line

print( '\n' + lines[0] + '\n' + lines[1] + '\n' + lines[2] + '\n' + lines[3] + '\n' + lines[4] + '\n' + lines[5]) #Print paragraph one by one with spaces